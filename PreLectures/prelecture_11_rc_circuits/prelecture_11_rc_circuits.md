# RC Circuits

## Overview
* Last time
  * Kirchhoff's Rules
      * Voltage Rule \[\sum \Delta V_n = 0\]
      * Current Rule \[\sum I_{in} = \sum I_{out}\]
  * Real Batteries
      * \[V_b = V_0 \frac{ \frac{ R}{ r}}{ 1 + \frac{ R}{ r}\]
* Today we discuss _RC Circuits_
    * [[/images/rc_circuit.png]] 
    * Start with a circuit that charges a battery through a resistor.
    * Move on to a circuit that removes the battery so the capacitor is
      discharged.
    * Close by discussing the energy flow in these circuits.

## Charging Capacitor: Qualitative Description
* Simple circuit containign a battery, capacitor and resistor.
* Last time we saw the circuit with just a battery and a capacitor that
  * \[V_b = V_c\]
  * \[q = C V_C\]
  * [[capcitor_only.png]]
  * This was viewed as being charged instantaneously after the battery was connected to it.
* We now look at adding a resistor to the circuit.
  * [[qualitative_circuit.png]]
  * This will limit the rate at which charge will flow to the capacitor and hence the 
    rate at which the voltage accross the capacitor is able to be charged.
  * We now close the gate and charge begins to flow
      * [[capcitor_and_resistor_t0.png]]
  * We now try to understand the magnitude and direction of this current 
    as a function of time.
      * Recall the voltage drop accross a capacitor is equal to the 
        charge over it's capacitance.
            * \[V_C = \frac{ q}{ C}\]
  * Initially the voltage across the capacitor is zero \[V_C( 0) = 0\]
      * At \[t = 0\] the circuit looks like it only contains a battery and a resistor.
      * Hence \[I(0) = \frac{ V_b}{ R}\]
  * As current continues to flow the top plate become positively charged and the bottom
    plate becomes negatively charched.
      * In turn a non zero voltage develops accross the capacitor.
      * This results in a reduced voltage accross the resistor as well.
      * By Kirchhoff's voltage rules the sum of the must equal the battery voltage.
      * Assentonically the current goes to zero as the charge on the capacitor approaches
        it's maximum value.
[[qualitative_summary.png]]

## Question 1
In our discussion of RC circuits we approached the problem as though current was 
actually flowing through the capacitor. On the other hand, it seems like the 
construction of a parallel plate capacitor should not allow actual charge to 
move across the gap between the plates. How can we explain this apparent paradox?

[[q1.png]]

* Charge flows into the top of the capacitor and out of the bottom of the capacitor, 
  but no charge actually crosses the gap between the plates.
  * Charge flows from the positive (top) terminal of the battery to the top plate of 
    the capacitor. Since the battery has to remain neutral at all times, exactly the 
    same amount of charge is pulled from the bottom plate of the capacitor and into the 
    negative (bottom) terminal of the battery. The result is that the top and bottom 
    plates of the capacitor always hold equal and opposite charge, the current is equal 
    in all parts of the circuit, and no actual charge is moving accross the gap of the 
    capacitor.
