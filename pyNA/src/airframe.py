import numpy as np
import pdb
import json

class Airframe:

    def __init__(self, pyna_directory, ac_name, case_name) -> None:
        
        # Settings 
        self.pyna_directory = pyna_directory
        self.ac_name = ac_name
        self.case_name = case_name
        
        self.aero = dict()

        self.path = self.pyna_directory + '/cases/' + self.case_name + '/aircraft/' + self.ac_name + '.json'
        
        with open(self.path) as f:
            params = json.load(f)

        Airframe.set_aircraft_parameters(self, **params)

    def set_aircraft_parameters(self, mtow: np.float64, n_eng: np.int64, comp_lst: list, af_S_h: np.float64, af_S_v: np.float64, 
                                af_S_w: np.float64, af_b_f: np.float64, af_b_h: np.float64, af_b_v: np.float64, af_b_w: np.float64, 
                                af_S_f: np.float64, af_s: np.int64, af_d_mg: np.float64,  af_d_ng: np.float64, af_l_mg:np.float64, 
                                af_l_ng: np.float64, af_n_mg: np.float64,  af_n_ng: np.float64, af_N_mg: np.float64, af_N_ng: np.float64, 
                                c_d_g: np.float64, mu_r: np.float64,  B_fan: np.int64,  V_fan: np.int64, RSS_fan: np.float64, M_d_fan: np.float64, 
                                inc_F_n: np.float64,  TS_lower: np.float64, TS_upper: np.float64, af_clean_w: bool, af_clean_h:bool, af_clean_v: bool, 
                                af_delta_wing: bool,  alpha_0: np.float64) -> None:
        """
        Set the aircraft parameters in the aircraft class.

        :param mtow: Max. take-off weight [kg]
        :type mtow: np.float64
        :param n_eng: Number of engines installed on the aircraft [-]
        :type n_eng: np.int64
        :param comp_lst: List of airframe components to include [-]
        :type comp_lst: list
        :param af_S_h: Horizontal tail area [m2]
        :type af_S_h: np.float64
        :param af_S_v: Vertical tail area [m2]
        :type af_S_v: np.float64
        :param af_S_w: Wing area [m2]
        :type af_S_w: np.float64
        :param af_b_f: Flap span [m]
        :type af_b_f: np.float64
        :param af_b_h: Horizontal tail span [m]
        :type af_b_h: np.float64
        :param af_b_v: Vertical tail span [m]
        :type af_b_v: np.float64
        :param af_b_w: Wing span [m]
        :type af_b_w: np.float64
        :param af_S_f: Flap area [m2]
        :type af_S_f: np.float64
        :param af_s: Number of slots for trailing-edge flaps (min. is 1) [-]
        :type af_s: np.int64
        :param af_d_mg: Tire diameter of main landing gear [m]
        :type af_d_mg: np.float64
        :param af_d_ng: Tire diameter of nose landing gear [m]
        :type af_d_ng: np.float64
        :param af_l_mg: Main landing-gear strut length [m]
        :type af_l_mg: np.float64
        :param af_l_ng: Nose landing-gear strut length [m]
        :type af_l_ng: np.float64
        :param af_n_mg: Number of wheels per main landing gear [-]
        :type af_n_mg: np.int64
        :param af_n_ng: Number of wheels per nose landing gear [-]
        :type af_n_ng: np.int64
        :param af_N_mg: Number of main landing gear [-]
        :type af_N_mg: np.int64
        :param af_N_ng: Number of nose landing gear [-]
        :type af_N_ng: np.int64
        :param: c_d_g: Landing gear drag coefficient [-]
        :type c_d_g; np.float64 
        :param mu_r: Rolling resistance coefficient [-]
        :type mu_r: np.float64
        :param B_fan: Number of fan blades [-]
        :type B_fan: np.int64
        :param V_fan: Number of fan vanes [-]
        :type V_fan: np.int64
        :param RSS_fan: Rotor-stator spacing [%]
        :type RSS_fan: np.float64
        :param M_d_fan: Relative tip Mach number of fan at design [-]
        :type M_d_fan: np.float64
        :param inc_F_n: Thrust inclination angle [deg]
        :type inc_F_n: np.float64
        :param TS_lower: Min. power setting [-]
        :type TS_lower: np.float64
        :param TS_upper: Max. power setting [-]
        :type TS_upper: np.float64
        :param af_clean_w: Flag for clean wing configuration [-]
        :type af_clean_w: bool
        :param af_clean_h: Flag for clean horizontal tail configuration [-]
        :type af_clean_h: bool
        :param af_clean_v: Flag for clean vertical tail configuration [-]
        :type af_clean_v: bool
        :param af_delta_wing: Flag for delta wing configuration [-]
        :type af_delta_wing: bool
        :param alpha_0: Wing mounting angle [deg]
        :type alpha_0: np.float64

        :return: None
        """

        self.mtow = mtow
        self.n_eng = n_eng
        self.comp_lst = comp_lst
        self.af_S_h = af_S_h
        self.af_S_v = af_S_v
        self.af_S_w = af_S_w
        self.af_b_f = af_b_f
        self.af_b_h = af_b_h
        self.af_b_v = af_b_v
        self.af_b_w = af_b_w
        self.af_S_f = af_S_f
        self.af_s = af_s
        self.af_d_mg = af_d_mg
        self.af_d_ng = af_d_ng
        self.af_l_mg = af_l_mg
        self.af_l_ng = af_l_ng
        self.af_n_mg = af_n_mg
        self.af_n_ng = af_n_ng
        self.af_N_mg = af_N_mg
        self.af_N_ng = af_N_ng
        self.c_d_g = c_d_g       
        self.mu_r = mu_r
        self.B_fan = B_fan
        self.V_fan = V_fan
        self.RSS_fan = RSS_fan
        self.M_d_fan = M_d_fan
        self.inc_F_n = inc_F_n
        self.TS_lower = TS_lower
        self.TS_upper = TS_upper
        self.af_clean_w = af_clean_w
        self.af_clean_h = af_clean_h
        self.af_clean_v = af_clean_v
        self.af_delta_wing = af_delta_wing
        self.alpha_0 = alpha_0

        return None

    def get_aerodynamics_deck(self) -> None:
        """
        Load aerodynamic data from aerodynamics deck.

        :return: None
        """

        if self.ac_name == 'stca':
            # Load data 
            self.aero['alpha'] = np.array([-2.,  0.,  2.,  4.,  6.,  8., 10., 12., 15., 18., 21., 23., 25.])
            self.aero['theta_flaps'] = np.array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24., 26.])
            self.aero['theta_slats'] = np.array([-26., -24., -22., -20., -18., -16., -14., -12., -10.,  -8.,  -6., -4.,  -2.,   0.])
            self.aero['c_l'] = np.load(self.pyna_directory + '/cases/' + self.case_name + '/aircraft/c_l_stca.npy')
            self.aero['c_l_max'] = np.load(self.pyna_directory + '/cases/' + self.case_name + '/aircraft/c_l_max_stca.npy')
            self.aero['c_d'] = np.load(self.pyna_directory + '/cases/' + self.case_name + '/aircraft/c_d_stca.npy')

        elif self.ac_name == 'a10':
            self.aero['alpha'] = np.array([-2.,  0.,  2.,  4.,  6.,  8., 10., 12., 15., 18., 21., 23., 25.])
            self.aero['theta_flaps'] = np.array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24., 26.])
            self.aero['theta_slats'] = np.array([-26., -24., -22., -20., -18., -16., -14., -12., -10.,  -8.,  -6., -4.,  -2.,   0.])
            self.aero['c_l'] = np.load(self.pyna_directory + '/cases/' + self.case_name + '/aircraft/c_l_stca.npy')
            self.aero['c_l_max'] = np.load(self.pyna_directory + '/cases/' + self.case_name + '/aircraft/c_l_max_stca.npy')
            self.aero['c_d'] = np.load(self.pyna_directory + '/cases/' + self.case_name + '/aircraft/c_d_stca.npy')
            
            # self.aero['alpha'] = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            # self.aero['theta_flaps'] = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0])
            # self.aero['theta_slats'] = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0])
            # self.aero['c_l'] = np.load(self.pyNA_directory + '/cases/' + self.case_name + '/aircraft/c_l_a10.npy')
            # self.aero['c_l_max'] = np.load(self.pyNA_directory + '/cases/' + self.case_name + '/aircraft/c_l_max_a10.npy')
            # self.aero['c_d'] = np.load(self.pyNA_directory + '/cases/' + self.case_name + '/aircraft/c_d_a10.npy')
            
        else:
            raise ValueError('Invalid aircraft name specified.')

        return None