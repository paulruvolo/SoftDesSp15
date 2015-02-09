""" TODO: Put your header comment here """

import Image

def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth at most
        max_depth (see assignment writeup for definition of depth in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions) """
    # TODO: implement this
    pass

def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        The representation of the function f is a defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    # TODO: implement this
    pass

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].
    
        val: the value to remap 
        input_interval_start: the start of the interval that contains all possible values for val
        input_interval_end: the end of the interval that contains all possible values for val
        output_interval_start: the start of the interval that contains all possible output values
        output_inteval_end: the end of the interval that contains all possible output values
        returns: the value remapped from the input to the outptu interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    im = Image.new("RGB",(350,350))
    pixels = im.load()

    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            x = remap_interval(i,0,im.size[0],-1,1)
            y = remap_interval(j,0,im.size[1],-1,1)
            pixels[i,j] = (int(remap_interval(evaluate_random_function(red_function,x,y),-1,1,0,255)),
                           int(remap_interval(evaluate_random_function(green_function,x,y),-1,1,0,255)),
                           int(remap_interval(evaluate_random_function(blue_function,x,y),-1,1,0,255)))

    im.save('myart.png')