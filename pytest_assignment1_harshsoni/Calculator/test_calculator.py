from calculator import addition,subtraction,multiply,division
import pytest
def test_addition():
    x=0
    assert addition(4,5)==9
    assert addition(4,5)!=7
    assert addition(9,0)==9
    assert addition(9,0)!=0
    assert addition(8)==8
    assert addition('a')=="invalid testcase"

def test_subtraction():
    assert subtraction(4,5)==-1
    assert subtraction(4,5)!=9
    assert subtraction(9,0)==9
    assert subtraction(9,0)!=0
    assert subtraction(8)==8
    assert subtraction('a')=="invalid testcase"

def test_multiplication():
    assert multiply(4,5)==20
    assert multiply(4,5)!=7
    assert multiply(9,0)==0
    assert multiply(9,0)!=9
    assert multiply(8)==0
    assert multiply('ac')=="invalid testcase"

def test_division():
    assert division(20,5)==4
    assert division(8,1)!=7
    assert division(9,0)=="y cannot be zero invalid testcase"
    assert division(9,0)!=9
    assert division(8)==8
    assert division('ac')=="invalid testcase"
