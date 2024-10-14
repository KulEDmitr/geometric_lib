#include <iostream>
using namespace std;
int square(int a,int b){
    //На вход функция получает 2 параметра: a - основание треугольника , b - высота треугольника. Функция выводит площадь треугольника
    return (a*b)/2;
}
int perimetr(int a,int s1,int s2){
    //На вход функция получает 3 параметра: a - основание треугольника, s1 и s2 - оставшиеся стороны треугольника. Функция выводит периметр треугольника
    return (a+s1+s2);
}
int main(){
    int a,b,s1,s2,c = 0,d = 0;
    cin>>a>>b>>s1>>s2;
    c =  square(a,b);
    d =  perimetr(a,s1,s2);
}
