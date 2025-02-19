#include <iostream>
#include <cstring>
#include <memory>

class String{
    private:
    char *buffer;
    unsigned int size;

    public:
    String(const char *string) {
        size = std::strlen(string);
        buffer = new char[size+1];
        memcpy(buffer, string, size);
        buffer[size] = 0;
    }

    String(const String &other) = delete; // remove the default copy constructor

    ~String() {
        delete[] buffer;
    }

    char& operator[](unsigned int index) {
        if (index > size) {
            return buffer[size];
        }
        return buffer[index];
    }
    friend std::ostream& operator<<(std::ostream& stream, const String &string);
};

// overloading the << operator
std::ostream& operator<<(std::ostream& stream, const String &string) {
    stream << string.buffer;
    return stream;
}

int main() {
    String string = "Hello";
    std::cout << string << std::endl;
    return 0;
}