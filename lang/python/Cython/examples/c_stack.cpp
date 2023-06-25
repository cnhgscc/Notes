extern "C"{
    #include "c_stack.h"
}

C_Stack::C_Stack(){
    tail = new Node;
    tail->prev = NULL;
    tail->val = NULL;
};

C_Stack::~C_Stack(){
    Node* t;
    while(tail != NULL){
        t = tail;
        tail=tail->prev;
        delete t;
    };
};

void C_Stack::push(PyObject* val){
    Node* pt = tail;
    pt->prev = tail;
    pt->val = val;
    tail = pt;
};