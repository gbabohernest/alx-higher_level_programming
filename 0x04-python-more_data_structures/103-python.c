#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list - print basic info about a python list
* @p: a pointer to the list object
* return: nothing
*/

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf(" [ERROR] Invalid  List Object\n");
		return;
	}

	Py_ssize_t sizeOfList = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t counter;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sizeOfList);
	printf("[*] Allocated = %ld\n", allocated);

	counter = 0;

	while (counter < sizeOfList)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[counter];

		if (item == NULL)
		{
			printf("Element %ld: Unable to get element\n", counter);
			continue;
		}
		const char *typeName = item->ob_type->tp_name;

		printf("Element %ld: %s\n", counter, typeName);
		counter++;
	}
}



/**
* print_python_bytes - print basic info about python bytecode
* @p: a pointer to the bytecode object
* return: nothing
*/

void print_python_bytes(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf(" [ERROR] Invalid  Bytes Object\n");
		return;
	}

	Py_ssize_t sizeOfObj = ((PyVarObject *)p)->ob_size;
	const char *s_value = ((PyBytesObject *)p)->ob_sval;
	Py_ssize_t counter;

	printf("[.] bytes object info");
	printf("  Size: %ld\n", sizeOfObj);
	printf("  Trying string: %s\n", s_value);

	printf("  first %ld bytes: ", (sizeOfObj <= 10 ? sizeOfObj : 10));

	counter = 0;

	while (counter < sizeOfObj && counter < 10)
	{
		printf("%02hhx", s_value[counter]);
		if (counter + 1 < sizeOfObj && counter + 1 < 10)
		{
			printf(" ");
		}
		counter++;
	}
	printf("\n");
}
