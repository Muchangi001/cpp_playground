#include <iostream>
#include <cstring>
#include <memory>

class String
{
    private:
    char *buffer;
    unsigned int size;

    public:
    String(const char *string)
    {
        size = std::strlen(string);
        buffer = new char[size + 1];
        memcpy(buffer, string, size);
        buffer[size] = 0; // ensure the null terminating character is included
    }

    // overload the copy constructor to perform deep copy
    String(const String &other)
        : size(other.size)
    {
        buffer = new char[size + 1];
        memcpy(buffer, other.buffer, size + 1);
    }

    ~String()
    {
        delete[] buffer;
    }

    // overload the [] operator
    char& operator[](unsigned int index)
    {
        if (index > size) {
            return buffer[size];
        }
        return buffer[index];
    }

    // overload the << operator
    friend std::ostream& operator<<(const std::ostream& stream, const String &string);
};

// define the << operator overloading
std::ostream& operator<<(const std::ostream& stream, const String &string)
{
    stream << string.buffer;
    return stream;
}

int main()
{
    String string1 = "Hello";
    String string2 = string1; // performing deep copy
    string2[1] = 'a';
    std::cout << string1 << std::endl;
    std::cout << string2 << std::endl;
    return 0;
}