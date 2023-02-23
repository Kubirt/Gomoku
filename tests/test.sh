#!/bin/bash

clear
make

# test1
echo ""
echo "TEST 1"
cat tests/test1.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK"

if [ $returnValue != 0 ]; then
	echo -e "test 1: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 1: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 1 passed"
fi
echo ""

# test2
echo "TEST 2"
cat tests/test2.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="ERROR you must provide a size."

if [ $returnValue != 0 ]; then
	echo -e "test 2: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 2: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 2 passed"
fi
echo ""

# test3
echo "TEST 3"
cat tests/test3.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
2,4
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 3: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 3: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 3 passed"
fi
echo ""

# test4
echo "TEST 4"
cat tests/test4.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
2,4
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 4: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 4: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 4 passed"
fi
echo ""

# test5
echo "TEST 5"
cat tests/test5.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
2,2
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 2 0 0 0 -1
-1 0 0 1 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 5: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 5: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 5 passed"
fi
echo ""

# test6
echo "TEST 6"
cat tests/test6.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
4,3
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 1 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 6: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 6: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 6 passed"
fi
echo ""

# test7
echo "TEST 7"
cat tests/test7.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
3,3
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 1 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 7: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 7: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 7 passed"
fi
echo ""

# test8
echo "TEST 8"
cat tests/test8.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
10,10
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 8: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 8: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 8 passed"
fi
echo ""

# test9
echo "TEST 9"
cat tests/test9.txt | ./pbrain-gomoku-ai 1>tests/AI_output
returnValue=$?
output=`cat tests/AI_output`
expectedOutput="OK
3,3
4,3
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 0 0 0 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 1 1 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 2 0 0 -1
-1 0 0 0 0 0 0 0 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1"

if [ $returnValue != 0 ]; then
	echo -e "test 9: bad return value, GOT:\n$returnValue\n\nEXPECTED:\n84"
elif [ "$output" != "$expectedOutput" ]; then
	echo -e "test 9: bad output, GOT:\n$output\n\nEXPECTED:\n$expectedOutput"
else
	echo "test 9 passed"
fi
