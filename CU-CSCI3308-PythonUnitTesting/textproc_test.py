#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#NAME: Elijah Berumen
#FALL 2018 CSCI 3308

#BUGS FIXED

#1.) Bug in count vowels 3!=2. Changed the aeou in the regex portion to aeiou to include
#all vowels
#2.)The last portion of the regex phone number check in the phone number function
#should check for the third chunk of the number to have 4 digits instead of 3
#Lastly the regex should include 0-9 for digits not 1-9


import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...
    #all test cases will be having self as parameters?
    def testString(self):
        #sample num
        num = 1
        self.assertRaises(textproc.TextProcError, lambda: textproc.Processor(num))
    #counts characters
    def testCount(self):
        expected = 8
        p = textproc.Processor("software")
        result = p.count()
        self.assertEqual(expected, result)
        #counts only letters
    def testCountAlpha(self):
        expected = 10
        p = textproc.Processor("eliberumen27")
        result = p.count_alpha()
        self.assertEqual(expected, result)
        #counts numbers
    def testCountNumeric(self):
        expected = 2
        p = textproc.Processor("eliberumen27")
        result = p.count_numeric()
        self.assertEqual(expected, result)
        #counts vowels
    def testCountVowels(self):
        expected = 3
        p = textproc.Processor("elijah")
        result = p.count_vowels()
        self.assertEqual(expected, result)
        #checks if phone number
    def testPhonenumber(self):
        expected = True
        p = textproc.Processor("720-556-5021")
        result = p.is_phonenumber()
        self.assertEqual(expected, result)


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
