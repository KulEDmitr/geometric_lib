#include <bin/rectangle.h>
#include <bin/triangle.h>
#include <gtest/gtest.h>

TEST(RectangleSquareTest, NormalTest){
    ASSERT_EQ(RectangleSquare(4, 5), 20);
}

TEST(RectangleSquareTest, BigDataTest){
    ASSERT_EQ(RectangleSquare(1000000000,1000), 1000000000000);
}

TEST(RectangleSquareTest, NegativeTest){
    ASSERT_EQ(RectangleSquare(-20,1000), 20000);
}

TEST(RectanglePerimetrTest, NormalTest){
    ASSERT_EQ(RectanglePerimetr(10,10), 40);
}

TEST(RectanglePerimetrTest, BigDataTest){
    ASSERT_EQ(RectanglePerimetr(1000000000,1000000000), 2000000000);
}

TEST(RectanglePerimetrTest, NegativeTest){
    ASSERT_EQ(RectanglePerimetr(-4, 5), 18);
}

TEST(TriangleSquareTest, NormalTest){
    ASSERT_EQ(TriangleSquare(5, 10), 25);
}

TEST(TriangleSquareTest, BigDataTest){
    ASSERT_EQ(TriangleSquare(1000000, 10000), 5000000000);
}

TEST(TriangleSquareTest, NegativeTest){
    ASSERT_EQ(TriangleSquare(-5, 10), 25);
}

TEST(TrianglePerimetrTest, NormalTest){
    ASSERT_EQ(TrianglePerimetr(5, 10, 5), 20);
}

TEST(TrianglePerimetrTest, BigDataTest){
    ASSERT_EQ(TrianglePerimetr(1000000000, 1000000000, 1000000000), 3000000000);
}

TEST(TrianglePerimetrTest, NegativeTest){
    ASSERT_EQ(TrianglePerimetr(-5, 10, 5), 30);
}