# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#   OpenBench is a chess engine testing framework authored by Andrew Grant.   #
#   <https://github.com/AndyGrant/OpenBench>           <andrew@grantnet.us>   #
#                                                                             #
#   OpenBench is free software: you can redistribute it and/or modify         #
#   it under the terms of the GNU General Public License as published by      #
#   the Free Software Foundation, either version 3 of the License, or         #
#   (at your option) any later version.                                       #
#                                                                             #
#   OpenBench is distributed in the hope that it will be useful,              #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU General Public License for more details.                              #
#                                                                             #
#   You should have received a copy of the GNU General Public License         #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

USE_CROSS_APPROVAL = False

OPENBENCH_CONFIG = {

    # Server Client version control
    'client_version' : '2',

    # Generic Error Messages useful to those setting up their own instance
    'error' : {
        'disabled' : 'Account has not been enabled. Contact andrew@grantnet.us',
        'fakeuser' : 'This is not a real OpenBench User. Create an OpenBench account',
    },

    # Link to the repo on the sidebar, as well as the core files
    'framework' : 'http://github.com/AndyGrant/OpenBench/',
    'corefiles' : 'https://raw.githubusercontent.com/AndyGrant/OpenBench/master/CoreFiles',

    # Test Configuration. For both SPRT and Fixed Games Tests

    'tests' : {
        'max_games'  : '20000',        # Default for Fixed Games
        'confidence' : '[0.05, 0.05]', # SPRT Type I/II Confidence
        'throughput' : { 'stc' : 1000, 'ltc' : 500, 'smpstc' : 1000, 'smpltc' : 500 },
    },

    # Book Configuration. When addding a book, follow the provided template.
    # The SHA is defined by hashlib.sha256(book).hexdigest(). Client.py has
    # code to generate and verify sha256 values, as an example.

    'books' : {

        '2moves_v1.epd' : {
            'name'    : '2moves_v1.epd',
            'sha'     : '7bec98239836f219dc41944a768c0506abed950aaec48da69a0782643e90f237',
            'source'  : 'https://raw.githubusercontent.com/AndyGrant/OpenBench/master/Books/2moves_v1.epd.zip',
            'default' : False,
        },

        '8moves_v3.epd' : {
            'name'    : '8moves_v3.epd',
            'sha'     : '1f055af431656f09ee6a09d2448e0b876125f78bb7b404fca2031c403a1541e5',
            'source'  : 'https://raw.githubusercontent.com/AndyGrant/OpenBench/master/Books/8moves_v3.epd.zip',
            'default' : False,
        },

        '3moves_FRC.epd' : {
            'name'    : '3moves_FRC.epd',
            'sha'     : '6bf81e1ada6a3306bbc8356f7bca1e2984a2828d658799992d5443b7179c934d',
            'source'  : 'https://raw.githubusercontent.com/AndyGrant/OpenBench/master/Books/3moves_FRC.epd.zip',
            'default' : False,
        },

        '4moves_noob.epd' : {
            'name'    : '4moves_noob.epd',
            'sha'     : '4be746a91e3f8af0c9344b1e72d611e9fcfe486843867a55760970a4896f284d',
            'source'  : 'https://raw.githubusercontent.com/AndyGrant/OpenBench/master/Books/4moves_noob.epd.zip',
            'default' : True,
        },
    },


    # Engine Configuration. All engines must have a name, a source repo,
    # a set of paramaters for each standard test type, as well as a scaled
    # NPS value, which is used to normalize speed across all workers.

    'engines' : {
        'princhess' : {

            'nps'       : 500000,
            'base'      : 'main',
            'bounds'    : '[-1.50, 4.50]',
            'source'    : 'https://github.com/princesslana/princhess',

            'build'     : {
                'path'      : '',
                'compilers' : ['cargo'],
                'cpuflags'  : [],
            },

            'testmodes' : {
                'stc'     : { 'threads' : 1, 'hash' : 128, 'timecontrol' : '10.0+0.1' },
                'ltc'     : { 'threads' : 1, 'hash' : 256, 'timecontrol' : '60.0+1.0' },
                'smpstc'  : { 'threads' : 2, 'hash' : 256, 'timecontrol' : '10.0+0.1' },
                'smpltc'  : { 'threads' : 2, 'hash' : 512, 'timecontrol' : '60.0+1.0' },
            },
        },
    },
}
