from distutils.core import setup, Extension

S4module = Extension('S4',
	sources = [
		'S4/main_python.c'
	],
	libraries = [
		'S4',
		'stdc++',
		'openblas',
	],
	library_dirs = ['./build',
					'/home/giovi/local_lib/usr/lib64',
					'/home/giovi/anaconda3/lib',
					'/usr/lib64'],
	runtime_library_dirs = ['/home/giovi/local_lib/usr/lib64',
							'/home/giovi/anaconda/lib',
							'/usr/lib64'],
	include_dirs = ['/home/giovi/local_lib/usr/include'],
	extra_link_args = [
		'./build/libS4.a'
	]
)

setup(name = 'S4',
	version = '1.1',
	description = 'Stanford Stratified Structure Solver (S4): Fourier Modal Method',
	ext_modules = [S4module]
)
