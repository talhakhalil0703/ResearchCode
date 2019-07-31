class Patient:
    def __init__(self, name):
        self.name = name
        self.mm_files = []
        self.mm_files_names = []

class MM:
    def __init__(self, name):
        self.name = name
        self.segments = []

class SegmentFile:
    def __init__(self,name):
        self.name = name
        self.exponent = None
        self.offset = None
        self.r2 = None
        self.error = None
        self.peak_freq = []
        self.freq_area = []

class BrainSection:
    def __init__(self, name):
        self.name = name
        self.average_exponents = []
        self.average_offset = []
        self.average_r2 = []
        self.average_error = []
        self.peak_freq = []
        self.freq_area = []
        self.beta_freq_area = []
        self.low_beta_freq_area = []
        self.high_beta_freq_area = []
        self.alpha_freq_area = []
        self.delta_freq_area = []
        self.theta_freq_area = []
        self.gamma_freq_area = []
