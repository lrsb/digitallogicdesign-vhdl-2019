from vunit import VUnit

prj = VUnit.from_argv()
lib = prj.add_library("lib")
lib.add_source_files("./*.vhd")
prj.main()
