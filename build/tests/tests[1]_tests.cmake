add_test([=[TriangleTestSuite.Area1]=]  [==[/home/littleking08/ИСРПО/geometric_lib/build/tests/tests]==] [==[--gtest_filter=TriangleTestSuite.Area1]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[TriangleTestSuite.Area1]=]  PROPERTIES WORKING_DIRECTORY [==[/home/littleking08/ИСРПО/geometric_lib/build/tests]==] SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[TriangleTestSuite.Area2]=]  [==[/home/littleking08/ИСРПО/geometric_lib/build/tests/tests]==] [==[--gtest_filter=TriangleTestSuite.Area2]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[TriangleTestSuite.Area2]=]  PROPERTIES WORKING_DIRECTORY [==[/home/littleking08/ИСРПО/geometric_lib/build/tests]==] SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[TriangleTestSuite.Perimeter1]=]  [==[/home/littleking08/ИСРПО/geometric_lib/build/tests/tests]==] [==[--gtest_filter=TriangleTestSuite.Perimeter1]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[TriangleTestSuite.Perimeter1]=]  PROPERTIES WORKING_DIRECTORY [==[/home/littleking08/ИСРПО/geometric_lib/build/tests]==] SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
add_test([=[TriangleTestSuite.Perimeter2]=]  [==[/home/littleking08/ИСРПО/geometric_lib/build/tests/tests]==] [==[--gtest_filter=TriangleTestSuite.Perimeter2]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[TriangleTestSuite.Perimeter2]=]  PROPERTIES WORKING_DIRECTORY [==[/home/littleking08/ИСРПО/geometric_lib/build/tests]==] SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
set(  tests_TESTS TriangleTestSuite.Area1 TriangleTestSuite.Area2 TriangleTestSuite.Perimeter1 TriangleTestSuite.Perimeter2)