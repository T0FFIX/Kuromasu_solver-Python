#include <iostream>
#include <string>
#include <fstream>


using namespace std;

int main()
{

    cout << "Hello World!" << endl;


    return 0;
}


int checkQuality(int numberOfMoves)
{
    int qualityNumber;



    return qualityNumber;
}

string extractMap(int mapNumber)
{
    string extension = ".txt";
    string path = "maps/" + mapNumber + extension;

    ifstream openMap;
    openMap.open(path);

    string mapInformation; 
    getline(openMap, mapInformation);
    openMap.close();
    return mapInformation;
}
