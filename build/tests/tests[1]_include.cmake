if(EXISTS "/home/littleking08/ИСРПО/geometric_lib/build/tests/tests[1]_tests.cmake")
  include("/home/littleking08/ИСРПО/geometric_lib/build/tests/tests[1]_tests.cmake")
else()
  add_test(tests_NOT_BUILT tests_NOT_BUILT)
endif()
