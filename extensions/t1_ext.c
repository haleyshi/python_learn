#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int fac(int n)
{
    if (n < 2) return (1);
    return (n) * fac(n-1);
}

char *reverse(char *s)
{
    register char t,                     // tmp
            *p = s,                      // fwd
            *q = (s + strlen(s) - 1);    // bwd

    while (p < q)  // swap and move ptrs
    {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }

    return s;
}

int test()
{
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));

    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));

    return 0;
}

#include "Python.h"

static PyObject * Test1_fac(PyObject *self, PyObject *args)
{
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))   // Convert python int to C int
        return NULL;

    return (PyObject*)Py_BuildValue("i", fac(num));  // Convert from C int to Python int
}

static PyObject * Test1_doppel(PyObject *self, PyObject *args)
{
    char *orig_str;
    char *dupe_str;
    PyObject* retval;

    // PyArg_ParseTupleAndKeywords: parse parms in tuple and keywords
    if (!PyArg_ParseTuple(args, "s", &orig_str))   // covert python str to C str
        return NULL;
    retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));  // Convert 2 C strings to Python Strings
    free(dupe_str);
    return retval;
}

static PyObject * Test1_test(PyObject *self, PyObject *args)
{
    test();
    return (PyObject*)Py_BuildValue("");
}

static PyMethodDef Test1Methods[] = {
    {"fac", Test1_fac, METH_VARARGS},   // METH_VARARGS: parms tuple, METH_KEYWORDS: parms in keywords, METH_VARARGS | METH_KEYWORDS
    {"doppel", Test1_doppel, METH_VARARGS},
    {"test", Test1_test, METH_VARARGS},
    {NULL, NULL}   // End of Method Defs
};

void initTest1()
{
    Py_InitModule("Test1", Test1Methods);
}