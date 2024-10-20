#!/usr/bin/env python3
'''
config file for rcfuzz
'''
import os
import sys
import tempfile
from typing import Dict

# FIXME
if not __package__:
    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    __package__ = "rcfuzz"

INPUT_DIR = 'queue'
CRASH_DIR = 'crashes'

# NOTE: you can define your own config
CONFIG: Dict = {
    # these will be default parameters for cli.py
    'scheduler': {
        'explore_time': 600,
        'exploit_time': 600,
        'coverage_update_time': 30,
        'sync_time': 300,
        'timeout': '24h'
    },
    # unused now
    'docker': {
        'root_dir': '/work/rcfuzz',
        'network': 'rcfuzz'
    },
    # binary directories for AFL-compiled binaries
    # justafl is used to get AFL bitmap
    # aflasan is used to triage crashes/bugs
    'evaluator': {
        'binary_root': '/out/afl',
        'binary_crash_root': '/out/aflasan',
    },
    # only specify basic things
    # how to launch fuzzers with proper arguments is handled by fuzzer driver
    'fuzzer': {
        'afl': {
            'input_dir': INPUT_DIR, # queue dir
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'command': '/out/fuzzers/afl/afl-fuzz', # fuzzer binary path
            'target_root': '/out/afl', # which binary is used to fuzz
            'afl_based': True,
        },
        'aflfast': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'command': '/out/fuzzers/aflfast/afl-fuzz',
            'target_root': '/out/afl',
            'afl_based': True
        },
        'fairfuzz': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'command': '/out/fuzzers/afl-rb/afl-fuzz',
            'target_root': '/out/afl',
            'afl_based': True
        },
        'mopt': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'command': '/out/fuzzers/MOpt-AFL/MOpt/afl-fuzz',
            'target_root': '/out/afl',
            'afl_based': True,
        },
        'learnafl': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'command': '/out/fuzzers/LearnAFL/afl-fuzz',
            'target_root': '/out/afl',
            'afl_based': True
        },
        'qsym': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'afl_based': True,
            'target_root': '/d/p/normal',  # for qsym
            # afl_command # reuse base afl
            'qsym_command': '/out/fuzzers/qsym/bin/run_qsym_afl.py'
        },
        'lafintel': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'command': '/out/fuzzers/aflpp/afl-fuzz',
            'target_root': '/out/lafintel',
            'afl_based': True
        },
        'redqueen': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'target_root': '/out/aflpp',
            'target_root_cmp': '/', # NO
            'command': '/out/fuzzers/aflpp/afl-fuzz',
            'afl_based': True
        },
        'radamsa': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'skip_crash_file': ['README.txt'],
            'target_root': '/out/aflpp',
            'command': '/out/fuzzers/aflpp/afl-fuzz',
            'aflpp_dir': '/fuzzer/afl++',
            'afl_based': True
        },
        'angora': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'create_output_dir': False,
            'target_root': '/out/angora', # NO
            'target_root_taint': '/d/p/angora/taint',
            'command': '/out/fuzzers/angora/angora_fuzzer',
            'afl_based': False,
        },
        'libfuzzer': {
            'input_dir': INPUT_DIR,
            'crash_dir': CRASH_DIR,
            'target_root': '/out/libfuzzer',
            'skip_crash_file': ['README.txt'],
            'command': None,  # target as fuzzer
            'afl_based': False
        }
    },
    # each target has a group like unibench/fuzzer-test-suite
    'target': {
        'bloaty_fuzz_target': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzz_target',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'bloaty_fuzz_target_52948c': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzz_target',
            'type': 'bug',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'curl_curl_fuzzer_http': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'curl_fuzzer_http',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'freetype2_ftfuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'ftfuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'harfbuzz_hb-shape-fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'hb-shape-fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'harfbuzz_hb-shape-fuzzer_17863b': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'hb-shape-fuzzer',
            'type': 'bug',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'jsoncpp_jsoncpp_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'jsoncpp_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'lcms_cms_transform_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'cms_transform_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'libjpeg-turbo_libjpeg_turbo_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'libjpeg_turbo_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'libpcap_fuzz_both': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzz_both',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'libpng_libpng_read_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'libpng_read_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'libxml2_xml': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'xml',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'libxml2_xml_e85b9b': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'xml',
            'type': 'bug',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'libxslt_xpath': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'xpath',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'mbedtls_fuzz_dtlsclient': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzz_dtlsclient',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'mbedtls_fuzz_dtlsclient_7c6b0e': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzz_dtlsclient',
            'type': 'bug',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'mruby_mruby_fuzzer_8c8bbd': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'mruby_fuzzer',
            'type': 'bug',
            'dict': 'mruby.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'openh264_decoder_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'decoder_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'openssl_x509': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'openssl',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'openthread_ot-ip6-send-fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'ot-ip6-send-fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'php_php-fuzz-parser_0dbedb': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'php-fuzz-parser',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': ['lafintel']
        },
        'proj4_proj_crs_to_crs_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'proj_crs_to_crs_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        're2_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'sqlite3_ossfuzz': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'ossfuzz',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'stb_stbi_read_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'stb_stbi_read_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': ['lafintel']
        },
        'systemd_fuzz-link-parser': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'fuzz-link-parser',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'vorbis_decode_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'decode_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'woff2_convert_woff2ttf_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'convert_woff2ttf_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        },
        'zlib_zlib_uncompress_fuzzer': {
            'group': 'fuzzbench',
            'seed': '',
            'fuzz_target': 'zlib_uncompress_fuzzer',
            # 'dict': 'jpeg.dict',
            'args': {
                'default': '@@',
            },
            'unsupported': []
        }
        # 'exiv2': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/jpg',
        #     'code_dir': 'unibench/exiv2-0.26',
        #     'input_model': 'jpeg.xml',
        #     'dict': 'jpeg.dict',
        #     # default is AFL-style (@@ for input file)
        #     'args': {
        #         'default': '@@',
        #     },
        #     # fuzzers that do not support this target.
        #     # rcfuzz will do some sanity check when started.
        #     'unsupported': ['libfuzzer']
        # },
        # 'gdk-pixbuf-pixdata': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/jpg',
        #     'code_dir': 'unibench/gdk-pixbuf-2.31.1',
        #     'input_model': 'jpeg.xml',
        #     'dict': 'jpeg.dict',
        #     'args': {
        #         'default': '@@ /dev/null',
        #     },
        #     'unsupported': ['libfuzzer', 'angora', 'qsym']
        # },
        # 'imginfo': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/jpg',
        #     'code_dir': 'unibench/jasper-2.0.12',
        #     'input_model': 'jpeg.xml',
        #     'dict': 'jpeg.dict',
        #     'args': {
        #         'default': '-f @@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'jhead': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/jpg',
        #     'code_dir': 'unibench/jhead-3.00',
        #     'input_model': 'jpeg.xml',
        #     'dict': 'jpeg.dict',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'tiffsplit': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/tiff',
        #     'dict': 'tiff.dict',
        #     'code_dir': 'unibench/libtiff-3.9.7',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'lame': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/mp3',
        #     'code_dir': 'unibench/lame-3.99.5',
        #     'input_model': 'mp3.xml',
        #     'args': {
        #         'default': '@@ /dev/null',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'mp3gain': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/mp3',
        #     'code_dir': 'unibench/mp3gain-1.5.2',
        #     'input_model': 'mp3.xml',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'wav2swf': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/wav',
        #     'input_model': 'wav.xml',
        #     'dict': 'wav.dict',
        #     'code_dir': 'unibench/swftools-0.9.2',
        #     'args': {
        #         'default': '-o /dev/null @@',
        #     },
        #     'unsupported': ['libfuzzer', 'angora']
        # },
        # 'ffmpeg': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/mp4',
        #     'input_model': 'mp4.xml',
        #     'code_dir': 'unibench/ffmpeg-4.0.1',
        #     'args': {
        #         'default': '-y -i @@ -c:v mpeg4 -c:a copy -f mp4 /dev/null',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'flvmeta': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/flv',
        #     'code_dir': 'unibench/flvmeta-1.2.1',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'mp42aac': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/mp4',
        #     'input_model': 'mp4.xml',
        #     'code_dir': 'unibench/Bento4-1.5.1-628',
        #     'args': {
        #         'default': '@@ /dev/null',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'cflow': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/text',
        #     'code_dir': 'unibench/cflow-1.6',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'infotocap': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/text',
        #     'code_dir': 'unibench/ncurses-6.1',
        #     'args': {
        #         'default': '-o /dev/null @@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'jq': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/text',
        #     'dict': 'json.dict',
        #     'code_dir': 'unibench/jq-1.5',
        #     'args': {
        #         'default': '. @@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'mujs': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/text',
        #     'code_dir': 'unibench/mujs-1.0.2',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'pdftotext': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/pdf',
        #     'input_model': 'pdf.xml',
        #     'dict': 'pdf.dict',
        #     'code_dir': 'unibench/xpdf-4.00',
        #     'args': {
        #         'default': '@@ /dev/null',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'sqlite3': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/pdf',
        #     'dict': 'sql.dict',
        #     'code_dir': 'unibench/SQLite-3.8.9',
        #     'args': {
        #         'default': '',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'nm': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/obj',
        #     'input_model': 'elf.xml',
        #     'dict': 'elf.dict',
        #     'code_dir': 'unibench/binutils-5279478',
        #     'args': {
        #         'default':
        #         '-A -a -l -S -s --special-syms --synthetic --with-symbol-versions -D @@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'objdump': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/obj',
        #     'input_model': 'elf.xml',
        #     'dict': 'elf.dict',
        #     'code_dir': 'unibench/binutils-2.28',
        #     'args': {
        #         'default': '-S @@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'tcpdump': {
        #     'group': 'unibench',
        #     'seed': '/seeds/unibench/general_evaluation/pcap',
        #     'input_model': 'pcap.xml',
        #     'code_dir': 'unibench/libpcap-1.8.1',
        #     'args': {
        #         'default': '-e -vv -nr @@',
        #     },
        #     'unsupported': ['libfuzzer']
        # },
        # 'boringssl-2016-02-12': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/boringssl-2016-02-12',
        #     'code_dir': 'fuzzer-test-suite-build/boringssl-2016-02-12',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'c-ares-CVE-2016-5180': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/c-ares-CVE-2016-5180',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'freetype2-2017': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/freetype2-2017',
        #     'input_model': 'xtf.xml',
        #     'code_dir': 'fuzzer-test-suite-build/freetype2-2017',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'guetzli-2017-3-30': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/guetzli-2017-3-30',
        #     'code_dir': 'fuzzer-test-suite-build/guetzli-2017-3-30',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'harfbuzz-1.3.2': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/harfbuzz-1.3.2',
        #     'code_dir': 'fuzzer-test-suite-build/harfbuzz-1.3.2',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'json-2017-02-12': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/json-2017-02-12',
        #     'dict': 'json.dict',
        #     'code_dir': 'fuzzer-test-suite-build/json-2017-02-12',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'lcms-2017-03-21': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/lcms-2017-03-21',
        #     'code_dir': 'fuzzer-test-suite-build/lcms-2017-03-21',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'libarchive-2017-01-04': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/libarchive-2017-01-04',
        #     'code_dir': 'fuzzer-test-suite-build/libarchive-2017-01-04',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'libjpeg-turbo-07-2017': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/libjpeg-turbo-07-2017',
        #     'input_model': 'jpeg.xml',
        #     'dict': 'jpeg.dict',
        #     'code_dir': 'fuzzer-test-suite-build/libjpeg-turbo-07-2017',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'libpng-1.2.56': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/libpng-1.2.56',
        #     'input_model': 'png.xml',
        #     'dict': 'png.dict',
        #     'code_dir': 'fuzzer-test-suite-build/libpng-1.2.56',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'libssh-2017-1272': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/libssh-2017-1272',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'libxml2-v2.9.2': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'dict': 'xml.dict',
        #     'code_dir': 'fuzzer-test-suite-build/libxml2-v2.9.2',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'llvm-libcxxabi-2017-01-27': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/llvm-libcxxabi-2017-01-27',
        #     'args': {
        #         'default': '@@',
        #     },
        #     'unsupported': ['afl']
        # },
        # 'openssl-1.0.1f': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/openssl-1.0.1f',
        #     'code_dir': 'fuzzer-test-suite-build/openssl-1.0.1f',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'openssl-1.0.2d': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/openssl-1.0.2d',
        #     'code_dir': 'fuzzer-test-suite-build/openssl-1.0.2d',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'openssl-1.1.0c-bignum': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/openssl-1.1.0c-bignum',
        #     'code_dir': 'fuzzer-test-suite-build/openssl-1.1.0c',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'openssl-1.1.0c-x509': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/openssl-1.1.0c-x509',
        #     'code_dir': 'fuzzer-test-suite-build/openssl-1.1.0c',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'openthread-2018-02-27-radio': {
        #     'group': 'fuzzer-test-suite',
        #     'seed':
        #     '/seeds/fuzzer-test-suite/openthread-2018-02-27/seeds-radio',
        #     'code_dir': 'fuzzer-test-suite-build/openthread-2018-02-27',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'openthread-2018-02-27-ip6': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/openthread-2018-02-27',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'pcre2-10.00': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/pcre2-10.00',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'proj4-2017-08-14': {
        #     'group': 'fuzzer-test-suite',  # seed too big for AFL ( > 1M)
        #     # 'seed': '/seeds/fuzzer-test-suite/proj4-2017-08-14',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/proj4-2017-08-14',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 're2-2014-12-09': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'code_dir': 'fuzzer-test-suite-build/re2-2014-12-09',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'sqlite-2016-11-14': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/custom/empty',
        #     'dict': 'sql.dict',
        #     'code_dir': 'fuzzer-test-suite-build/sqlite-2016-11-14',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'vorbis-2017-12-11': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/vorbis-2017-12-11',
        #     'input_model': 'ogg.xml',
        #     'code_dir': 'fuzzer-test-suite-build/vorbis-2017-12-11',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'woff2-2016-05-06': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/woff2-2016-05-06',
        #     'code_dir': 'fuzzer-test-suite-build/woff2-2016-05-06',
        #     'args': {
        #         'default': '@@',
        #     }
        # },
        # 'wpantund-2018-02-27': {
        #     'group': 'fuzzer-test-suite',
        #     'seed': '/seeds/fuzzer-test-suite/wpantund-2018-02-27',
        #     'code_dir': 'fuzzer-test-suite-build/wpantund-2018-02-27',
        #     'args': {
        #         'default': '@@',
        #     }
        # }
    }
}

FUZZERS_AFL = [
    'afl', 'aflfast', 'fairfuzz', 'mopt', 'lafintel', 'learnafl', 'redqueen',
    'radamsa', 'qsym'
]

FUZZERS = [
    'afl', 'aflfast', 'fairfuzz', 'mopt', 'lafintel', 'learnafl', 'redqueen',
    'radamsa', 'qsym', 'angora', 'libfuzzer'
]

# Used by fuzz driver

AFL_MASTER_STR = 'afl-master'
AFL_SLAVE_STR = 'afl-slave'

# Use different directories every run
DATABASE_DIR = tempfile.mkdtemp()
