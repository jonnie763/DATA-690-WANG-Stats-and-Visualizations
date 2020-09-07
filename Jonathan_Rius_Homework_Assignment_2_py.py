{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Jonathan Rius- Homework Assignment #2.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyO+YYv615BfQ5tz9ukDZib/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jonnie763/DATA-690-WANG/blob/master/Jonathan_Rius_Homework_Assignment_2_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4Re-qT4UBt3X",
        "colab_type": "text"
      },
      "source": [
        "Jonathan Rius: Assignment #2\n",
        "1. Prompts a user to enter 10 integers.\n",
        "\n",
        "2. If the user enters anything other than integers, remind her that only integers are allowed and let her retry.\n",
        "\n",
        "3. Don't allow the user to enter more than 10 or less than 10 integers.\n",
        "\n",
        "4. Display the 10 integers back to the user at the end. Calculate the following statistics from the 10 integers entered *Minimum Maximum Range Mean Variance Standard Deviation*\n",
        "\n",
        "#I began the assignment by chunking the assignment into four parts; prompting the user, reminding the user, not allowing the user and calculation.                             "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7fy1gldsBd1d",
        "colab_type": "text"
      },
      "source": [
        "Revised Prompt For User"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BOUN6zty_l2m",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "outputId": "2b39c662-b612-4abf-f96d-2ff25f2ec89b"
      },
      "source": [
        "num_list = []\n",
        "\n",
        "while len(num_list) < 10:  \n",
        "\n",
        "    num = input(f\"\\nplease enter an integer ({len(num_list) + 1} of 10): \")\n",
        "\n",
        "    try:\n",
        "        num = int(num)\n",
        "        num_list.append(num)\n",
        "    except:\n",
        "        print(\"\\nYou have entered a non-integer. Please enter an integer.\")\n",
        "\n",
        "print(\"\\n\", num_list)\n",
        "\n",
        "# There are several things going on here, first prompting the user to input ten numbers is easy enough, but one needs to stop the user if he/she is inputting non-integers and only count integers towards the total ten integers.\n",
        "# The input adds to the total of 10 integers, the len num list code is to ensure the user doesn't go past 10 integers, and the except code is the reminder to make the user sticks to integers.  \n"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "please enter an integer (1 of 10): 100\n",
            "\n",
            "please enter an integer (2 of 10): 123\n",
            "\n",
            "please enter an integer (3 of 10): 123\n",
            "\n",
            "please enter an integer (4 of 10): 234\n",
            "\n",
            "please enter an integer (5 of 10): 234\n",
            "\n",
            "please enter an integer (6 of 10): 234\n",
            "\n",
            "please enter an integer (7 of 10): 345\n",
            "\n",
            "please enter an integer (8 of 10): 234\n",
            "\n",
            "please enter an integer (9 of 10): 456\n",
            "\n",
            "please enter an integer (10 of 10): 345\n",
            "\n",
            " [100, 123, 123, 234, 234, 234, 345, 234, 456, 345]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rNGg7dWfBlzT",
        "colab_type": "text"
      },
      "source": [
        "**Calculate** average,min, max, range"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RAN_2_BfBexE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        },
        "outputId": "7e43f204-2eae-4ce9-a9f0-876e52b6e7cd"
      },
      "source": [
        "total = 0\n",
        "for num in num_list:\n",
        "    total += num\n",
        "\n",
        "print(f\"Average = {total/len(num_list)}\" )\n",
        "print(f\"Minimum is:\", min(num_list))\n",
        "print(f\"Maximum is:\", max(num_list))\n",
        "print(f\"Range is\" ,(max(num_list))- min(num_list))\n",
        "\n",
        "# Average is total divided by lens which refers to amount of numbers in list, I just used min and max functions for min and max but applied to the num_list so the list above was being referred to. Range is simply max minus min. "
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Average = 242.8\n",
            "Minimum is: 100\n",
            "Maximum is: 456\n",
            "Range is 356\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kBnw7eY9BlaE",
        "colab_type": "text"
      },
      "source": [
        "**Caculate** Variance and Standard Deviation"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_B_GXtvnBh1R",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "a08beffa-82bb-4fa2-e5ac-4f51c4188b79"
      },
      "source": [
        "\n",
        "def mean(num_list):\n",
        "    \n",
        "    total = 0  \n",
        "\n",
        "    for num in num_list:\n",
        "        total += num\n",
        "\n",
        "    return total / len(num_list)\n",
        "\n",
        "\n",
        "def var(num_list):\n",
        "    \n",
        "    the_mean = mean(num_list)                     \n",
        "    \n",
        "    squared_diff = [(x - the_mean) ** 2 for x in num_list]    \n",
        "    \n",
        "    return mean(squared_diff)                   \n",
        "\n",
        "import math\n",
        "\n",
        "def std(num_list):\n",
        "    the_var = var(num_list)\n",
        "    return math.sqrt(the_var)\n",
        "\n",
        "\n",
        "the_std = std(num_list)\n",
        "\n",
        "print(\"std = \", round(the_std,2))\n",
        "print(\"var = \",round(the_std,2)**2)\n",
        "\n",
        "# First mean needs to be defined as it is the basis for the variance function \n",
        "# Then once the variance function is defined with the addition of the mean being defined, one can take the square root of the variance function by importing math. This gives you standard deviation. \n",
        "# After I apply a square power on the standard deviation to obtain the variance "
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "std =  107.59\n",
            "var =  11575.608100000001\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}