// g++ -o module_name.so -shared -fPIC -I${BOOST_INCLUDE_PATH} -I${PYTHON_INCLUED_PATH} -L${BOOST_LIB_DIR} -lbosst_python ${MY_SRC_FILES}

#include <boost/python.hpp>



BOOST_PYTHON_MODULE(test){
    using namespace boost::python;

}