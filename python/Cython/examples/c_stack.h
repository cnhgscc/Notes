#include "Python.h"

extern "C"{
    class C_Stack{
        private:

        struct Node {
            PyObject* val;
            Node* prev;
        };

        Node* tail;

        public:
        C_Stack();
        ~C_Stack();
        void push(PyObject*);
    };
}