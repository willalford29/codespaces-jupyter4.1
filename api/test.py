{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "051b24c3",
   "metadata": {},
   "outputs": [],
   "source": [
    ">>> assert sum([1, 2, 3]) == 6, \"Should be 6\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "88b7b661",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Everything passed\n"
     ]
    }
   ],
   "source": [
    "def test_sum():\n",
    "    assert sum([1, 2, 3]) == 6, \"Should be 6\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    test_sum()\n",
    "    print(\"Everything passed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a664b32d",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "Should be 6",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\1\\ipykernel_13716\\3915460295.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[0mtest_sum\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m     \u001b[0mtest_sum_tuple\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Everything passed\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\1\\ipykernel_13716\\3915460295.py\u001b[0m in \u001b[0;36mtest_sum_tuple\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mtest_sum_tuple\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[1;32massert\u001b[0m \u001b[0msum\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Should be 6\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAssertionError\u001b[0m: Should be 6"
     ]
    }
   ],
   "source": [
    "def test_sum():\n",
    "    assert sum([1, 2, 3]) == 6, \"Should be 6\"\n",
    "\n",
    "def test_sum_tuple():\n",
    "    assert sum((1, 2, 2)) == 6, \"Should be 6\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    test_sum()\n",
    "    test_sum_tuple()\n",
    "    print(\"Everything passed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fd1152a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E\n",
      "======================================================================\n",
      "ERROR: C:\\Users\\will (unittest.loader._FailedTest)\n",
      "----------------------------------------------------------------------\n",
      "AttributeError: module '__main__' has no attribute 'C:\\Users\\will'\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.001s\n",
      "\n",
      "FAILED (errors=1)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "True",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m True\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3465: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "\n",
    "    def test_sum(self):\n",
    "        self.assertEqual(sum([1, 2, 3]), 6, \"Should be 6\")\n",
    "\n",
    "    def test_sum_tuple(self):\n",
    "        self.assertEqual(sum((1, 2, 2)), 6, \"Should be 6\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d7d3fefa",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3285513286.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\will.alford\\AppData\\Local\\Temp\\1\\ipykernel_13716\\3285513286.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    pip install nose2\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "pip install nose2\n",
    "python -m nose2\n",
    ".F"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "39fb70b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_sum():\n",
    "    assert sum([1, 2, 3]) == 6, \"Should be 6\"\n",
    "\n",
    "def test_sum_tuple():\n",
    "    assert sum((1, 2, 2)) == 6, \"Should be 6\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d74100bb",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'my_sum'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\1\\ipykernel_15512\\2055765858.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0munittest\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mmy_sum\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msum\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'my_sum'"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "from my_sum import sum\n",
    "\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "    def test_list_int(self):\n",
    "        \"\"\"\n",
    "        Test that it can sum a list of integers\n",
    "        \"\"\"\n",
    "        data = [1, 2, 3]\n",
    "        result = sum(data)\n",
    "        self.assertEqual(result, 6)\n",
    "\n",
    "target = __import__(\"my_sum.py\")\n",
    "sum = target.sum\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5312f96d",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2615156077.py, line 15)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\will.alford\\AppData\\Local\\Temp\\1\\ipykernel_15512\\2615156077.py\"\u001b[1;36m, line \u001b[1;32m15\u001b[0m\n\u001b[1;33m    $ python -m unittest test\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "\n",
    "    def test_sum(self):\n",
    "        self.assertEqual(sum([1, 2, 3]), 6, \"Should be 6\")\n",
    "\n",
    "    def test_sum_tuple(self):\n",
    "        self.assertEqual(sum((1, 2, 2)), 6, \"Should be 6\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    \n",
    "   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb215b31",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
