#include <boost/python.hpp>

#include <Python.h>

char const* greet()
{
   return "hello, world";
}


BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}