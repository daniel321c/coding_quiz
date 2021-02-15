#include <iostream>
using namespace std;

class B
{
  public:
    virtual void print()
    {
        cout << "I am B" << endl;
    }
};
class D : public B
{
  public:
    void print()
    {
        cout << "I am D" << endl;
    }
};
void f(B &t)
{
    throw t;
}

B m;

int main()
{
    try
    {
        B *b = &m;
        b->print();
        D *d = dynamic_cast<D *>(b);
        d->print();
    }
    catch (...)
    {
        cout << "catch Error" << endl;
    }
}