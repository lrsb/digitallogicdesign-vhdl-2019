<h1 align="center">
<br>
<img src="https://github.com/lrsb/digitallogicdesign-vhdl-2019/blob/master/image.png" alt="Manhattan distance" width="200">
<br>
Digital logic design project
</h1>
<h3 align="center">A VHDL implementation of a Manhattan distance calculator.</h3>
<p align="center">
  <a href="#description">Description</a> •
  <a href="#testing">Testing</a> •
  <a href="#license">License</a>
</p>

[![Build Status](https://app.travis-ci.com/lrsb/digitallogicdesign-vhdl-2019.svg?branch=master)](https://app.travis-ci.com/lrsb/digitallogicdesign-vhdl-2019)

## Description

The component has the task of calculating, given a centroid, the `N = 8` centroids closest to it.\
The space consists of a `256x256` square and the coordinates are stored in a `RAM`, which is not part of the project.\
An input mask is also provided which is used to filter the centroids in memory, in fact only those whose corresponding bit is set to 1 will be considered.\
The output mask will highlight the closest centroid, having its corresponding bit set to one. The masks use a `Little-Endian` notation.

The component interface is:
```vhdl
entity project_reti_logiche is
    port (
        i_clk      : in std_logic;                      --In clock
        i_start    : in std_logic;                      --Start signal
        i_rst      : in std_logic;                      --Reset signal
        i_data     : in std_logic_vector(7 downto 0);   --RAM out data interface
        o_address  : out std_logic_vector(15 downto 0); --RAM in address interface
        o_en       : out std_logic;                     --RAM enable signal
        o_we       : out std_logic;                     --RAM write enable
        o_data     : out std_logic_vector(7 downto 0);  --RAM in data interface
        o_done     : out std_logic                      --Computation completed signal
    );
end entity;
```
To implement the specifications is used a finite state machine synchronized on the falling edge of the clock, in such a way as to be able to perform operations without being affected by the delays of the RAM. 
It would not have been possible to do this on the rising edge.

Some optimizations are put in place to minimize the number of clock cycle needed to output a result.\
For example is possible, when the input `Mask ∈ {0 ∨ 2^n , n ∈ [0, 7]}` complete the process without further ado, the condition checked is
```vhdl
if unsigned(i_data and std_logic_vector(signed(i_data) - 1)) = 0 then
-- Input mask contains less than 2 bits set to one => output the corresponding centroid
else
-- Input mask contains at least 2 bits set to one => futher computations are needed
end if;
```

## Testing

Extensive testing is put in place, also using [GHDL](https://github.com/ghdl/ghdl) on TravisCI.

To test the component, in addition to the test provided as an example, a C program is used to generate random tests' VHDL code. Also all edge cases are tested.\
It uses [Fisher–Yates shuffle algorithm](https://en.wikipedia.org/wiki/Fisher–Yates_shuffle) to generate the permutations.

## License

MIT
