#include "../lib/square.cpp"
#include <cmath>
#include <iostream>
#include <typeinfo>

void check_square_area(){
    try{
        square_area(32.0f);
        if(typeid(square_area(32.0f))==typeid(float)){
        std::cout<<"TEST_SQUARE_AREA_13 OK\n";
        }
        else{
            std::cout<<"TEST_SQUARE_AREA_13 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_SQUARE_AREA_13 Failed(RE)\n";
    }

    try{
        if(square_area(5)==5*5){
        std::cout<<"TEST_SQUARE_AREA_14 OK\n";
        }
        else{
            std::cout<<"TEST_SQUARE_AREA_14 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_SQUARE_AREA_14 Failed(RE)\n";
    }

    try{
        square_area(5,52,7.232,13);
        std::cout<<"TEST_SQUARE_AREA_15 Failed(RE)\n";
    }
    catch(...){
        std::cout<<"TEST_SQUARE_AREA_15 OK\n";
    }

    return;
}

void check_square_perimeter(){
    try{
        square_perimeter(2);
        if(typeid(square_perimeter(2))==typeid(double)){
        std::cout<<"TEST_SQUARE_PERIMETER_16 OK\n";
        }
        else{
            std::cout<<"TEST_SQUARE_PERIMETER_16 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_SQUARE_PERIMETER_16 Failed(RE)\n";
    }

    try{
        if(square_perimeter(10.6f)==10.6f*4){
        std::cout<<"TEST_SQUARE_PERIMETER_17 OK\n";
        }
        else{
            std::cout<<"TEST_SQUARE_PERIMETER_17 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_SQUARE_PERIMETER_17 Failed(RE)\n";
    }

    try{
        square_perimeter(5,52,7.232,13);
        std::cout<<"TEST_SQUARE_PERIMETER_18 Failed(RE)\n";
    }
    catch(...){
        std::cout<<"TEST_SQUARE_PERIMETER_18 OK\n";
    }

    return;
}