#include "../lib/rectangle.cpp"
#include <cmath>
#include <iostream>
#include <typeinfo>

void check_rectangle_area(){
    try{
        rectangle_area(4,5);
        if(typeid(rectangle_area(4,5))==typeid(float)){
        std::cout<<"TEST_RECTANGLE_AREA_7 OK\n";
        }
        else{
            std::cout<<"TEST_RECTANGLE_AREA_7 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_RECTANGLE_AREA_7 Failed(Runtime Error)\n";
    }

    try{
        if(rectangle_area(5,2)==5*2){
        std::cout<<"TEST_RECTANGLE_AREA_8 OK\n";
        }
        else{
            std::cout<<"TEST_RECTANGLE_AREA_8 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_RECTANGLE_AREA_8 Failed(Runtime Error)\n";
    }

    try{
        rectangle_area(5,52,7.232,13);
        std::cout<<"TEST_RECTANGLE_AREA_9 Failed(RE)\n";
    }
    catch(...){
        std::cout<<"TEST_RECTANGLE_AREA_9 OK\n";
    }

    return;
}

void check_rectangle_perimeter(){
    try{
        rectangle_perimeter(1,5);
        if(typeid(rectangle_perimeter(1,5))==typeid(double)){
        std::cout<<"TEST_RECTANGLE_PERIMETER_10 OK\n";
        }
        else{
            std::cout<<"TEST_RECTANGLE_PERIMETER_10 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_RECTANGLE_PERIMETER_10 Failed(Runtime Error)\n";
    }

    try{
        if(rectangle_perimeter(10,4)==2*(10+4)){
        std::cout<<"TEST_RECTANGLE_PERIMETER_11 OK\n";
        }
        else{
            std::cout<<"TEST_RECTANGLE_PERIMETER_11 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_RECTANGLE_PERIMETER_11 Failed(Runtime Error)\n";
    }

    try{
        rectangle_perimeter(5,52,7.232,13);
        std::cout<<"TEST_RECTANGLE_PERIMETER_12 Failed(RE)\n";
    }
    catch(...){
        std::cout<<"TEST_RECTANGLE_PERIMETER_12 OK\n";
    }

    return;
}