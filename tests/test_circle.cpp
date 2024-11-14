#include "../lib/circle.cpp"
#include <cmath>
#include <iostream>
#include <typeinfo>

void check_circle_area(){
    try{
        circle_area(4);
        if(typeid(circle_area(4))==typeid(double)){
        std::cout<<"TEST_CIRCLE_AREA_1 OK\n";
        }
        else{
            std::cout<<"TEST_CIRCLE_AREA_1 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_CIRCLE_AREA_1 Failed(Runtime Error)\n";
    }

    try{
        if(circle_area(5)==M_PI*5*5/2){
        std::cout<<"TEST_CIRCLE_AREA_2 OK\n";
        }
        else{
            std::cout<<"TEST_CIRCLE_AREA_2 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_CIRCLE_AREA_2 Failed(Runtime Error)\n";
    }

    try{
        circle_area(5,52,7.232,13);
        std::cout<<"TEST_CIRCLE_AREA_3 Failed(RE)\n";
    }
    catch(...){
        std::cout<<"TEST_CIRCLE_AREA_3 OK\n";
    }

    return;
}

void check_circle_perimeter(){
    try{
        circle_perimeter(1);
        if(typeid(circle_perimeter(1))==typeid(double)){
        std::cout<<"TEST_CIRCLE_PERIMETER_4 OK\n";
        }
        else{
            std::cout<<"TEST_CIRCLE_PERIMETER_4 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_CIRCLE_PERIMETER_4 Failed(Runtime Error)\n";
    }

    try{
        if(circle_perimeter(10)==2*M_PI*10){
        std::cout<<"TEST_CIRCLE_PERIMETER_5 OK\n";
        }
        else{
            std::cout<<"TEST_CIRCLE_PERIMETER_5 Failed(WA)\n";
        }
    }
    catch(...){
        std::cout<<"TEST_CIRCLE_PERIMETER_5 Failed(Runtime Error)\n";
    }

    try{
        circle_perimeter(5,52,7.232,13);
        std::cout<<"TEST_CIRCLE_PERIMETER_6 Failed(RE)\n";
    }
    catch(...){
        std::cout<<"TEST_CIRCLE_PERIMETER_6 OK\n";
    }

    return;
}