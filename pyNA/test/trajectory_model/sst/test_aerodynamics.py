import unittest
import pdb
import openmdao.api as om
import numpy as np
from pyNA.pyna import pyna
from pyNA.src.trajectory_model.sst.aerodynamics import Aerodynamics
from openmdao.utils.assert_utils import assert_check_partials


class TestAerodynamics(unittest.TestCase):

	def test_evaluate(self):
		
		py = pyna(trajectory_mode='model', 
				  case_name='stca',
				  engine_name='engine_derivative')

		nn = 1
		
		prob = om.Problem()
		prob.model.add_subsystem("a", Aerodynamics(vec_size=nn, extrapolate=True, method='cubic', aircraft=py.aircraft))
		prob.setup(force_alloc_complex=True)

		prob.set_val('a.alpha', np.linspace(1, 10, nn))
		prob.set_val('a.theta_flaps', np.ones(nn))
		prob.set_val('a.theta_slats', np.ones(nn))
		prob.run_model()

		self.assertAlmostEqual(prob.get_val('a.c_l')[0], -0.05445165484715201, 4)
		self.assertAlmostEqual(prob.get_val('a.c_d')[0], 0.010356828289943939, 4)
		self.assertAlmostEqual(prob.get_val('a.c_l_max')[0], 1.0688052273911788, 4)

	def test_partials(self):

		py = pyna(trajectory_mode='model', 
		 		  case_name='stca',
				  engine_name='engine_derivative')
		
		nn = 10
		
		prob = om.Problem()
		prob.model.add_subsystem("a", Aerodynamics(vec_size=nn, extrapolate=True, method='cubic', aircraft=py.aircraft))
		prob.setup(force_alloc_complex=True)

		prob.set_val('a.alpha', np.linspace(1, 10, nn))
		prob.set_val('a.theta_flaps', np.ones(nn))
		prob.set_val('a.theta_slats', np.ones(nn))
		prob.run_model()

		data = prob.check_partials(compact_print=True, method='cs')
		assert_check_partials(data, atol=1e-6, rtol=1e-6)

if __name__ == '__main__':
	unittest.main()