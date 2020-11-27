import sys
import logging
import warnings
from muscotf.musco.tf.compressor.compress import CompressorVBMF, compress_seq, compress_noseq
from muscotf.musco.tf.optimizer.trt import Optimizer

logging.disable(logging.CRITICAL)

if not sys.warnoptions:
    warnings.simplefilter("ignore")
