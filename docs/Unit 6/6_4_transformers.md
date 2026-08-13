# Transformers

## How a transformer works

A transformer is a device used to **change** the value of an **alternating potential difference** or **current**, using **induction**. A basic transformer consists of a **primary coil**, a **secondary coil**, and an **iron core** — iron is used because it is easily **magnetised**.

![Diagram showing the structure of a transformer with a primary coil, secondary coil, and an iron core with magnetic field lines.](../assets/images/page_405_image_1_v2.jpg)

*Structure of a transformer*

An **alternating current** is supplied to the **primary coil**. Because this current is continually **changing direction**, it produces a **changing magnetic field** around the primary coil. Since the iron core is easily magnetised, this changing field passes through it, so there is now a changing magnetic field inside the **secondary coil** too — this field **cuts** through the secondary coil and **induces a potential difference** in it. Because the magnetic field is continually changing, the induced potential difference is also **alternating**, with the same **frequency** as the current supplied to the primary coil. If the secondary coil is part of a **complete circuit**, this causes an **alternating current** to flow.

A transformer can change the **size** of an alternating voltage, and has a number of roles: increasing the potential difference of electricity before it is transmitted across the national grid, lowering the high voltage used in power lines to the lower voltages used in houses, and lowering mains voltage in adapters to the lower voltages used by many electronic devices.

A **step-up** transformer **increases** the potential difference of a power source, and has **more** turns on the secondary coil than on the primary coil. A **step-down** transformer **decreases** the potential difference of a power source, and has **fewer** turns on the secondary coil than on the primary coil.

## Transformer equations

### The transformer equation

The output potential difference (voltage) of a transformer depends on the number of turns on the primary and secondary coils, and on the input potential difference (voltage). It can be calculated using the transformer equation:

!!! note "Required formulae: the transformer equation"
    $$ \frac{\text{potential difference across primary coil}}{\text{potential difference across secondary coil}} = \frac{\text{number of turns on primary coil}}{\text{number of turns on secondary coil}} $$

    $$ \frac{V_p}{V_s} = \frac{N_p}{N_s} $$

    Where $V_p$ and $V_s$ are the potential difference (voltage) across the primary and secondary coils in volts (V), and $N_p$ and $N_s$ are the number of turns on the primary and secondary coils. This can also be flipped upside down, giving $\frac{V_s}{V_p} = \frac{N_s}{N_p}$.

These equations show that the **ratio** of the potential differences across the primary and secondary coils of a transformer is **equal** to the ratio of the number of turns on each coil. A step-up transformer **increases** the potential difference of a power source, and has **more turns** on the **secondary coil** than on the primary coil ($N_s > N_p$); a step-down transformer **decreases** the potential difference, and has **fewer turns** on the **secondary coil** than on the primary coil ($N_s < N_p$).

!!! example "Worked Example (calculation)"

    A transformer has 20 turns on the primary coil and 800 turns on the secondary coil. The input potential difference across the primary coil is 500 V.

    a) Calculate the output potential difference

    b) State what type of transformer it is

    ??? success "Answer (Part a):"

        **Step 1: List the known quantities**

        * Number of turns in primary coil, $N_p = 20$
        * Number of turns in secondary coil, $N_s = 800$
        * Voltage in primary coil, $V_p = 500\text{ V}$

        **Step 2: Write out the transformer equation**

        Use the version with the secondary coil quantities on the top, to minimise the amount of rearranging.

        $$ \frac{N_s}{N_p} = \frac{V_s}{V_p} $$

        **Step 3: Rearrange for $V_s$**

        $$ V_s = \frac{N_s}{N_p} \times V_p $$

        **Step 4: Substitute values into the equation**

        $$ V_s = \frac{800}{20} \times 500 = 20\ 000\text{ V} $$

    ??? success "Answer (Part b):"

        The transformer is a **step-up** transformer, since it has more turns on the secondary coil, and a greater secondary voltage.

!!! tip "Examiner Tips and Tricks"

    When you are using the transformer equation make sure you have used the same letter (p or s) in the **numerators** (top line) of the fraction and the same letter (p or s) in the **denominators** (bottom line) of the fraction. There will be less rearranging to do in a calculation if the variable which you are trying to find is on the numerator (top line) of the fraction. The individual loops of wire going around each side of the transformer should be referred to as turns and not coils.

### The ideal transformer equation

An **ideal** transformer would be **100% efficient**. Although transformers can increase the voltage of a power source, due to the **law of conservation of energy**, they cannot increase the power output — so, if a transformer is 100% efficient, the input power equals the output power.

!!! note "Required formulae: transformer power (100% efficiency)"
    $$ P = V \times I $$

    Where $P$ is power in watts (W), $V$ is potential difference in volts (V), and $I$ is current in amps (A). If a transformer is 100% efficient, then input power equals output power:

    $$ V_{p} \times I_{p} = V_{s} \times I_{s} $$

    Where $V_p$ and $I_p$ are the potential difference and current for the primary coil, and $V_s$ and $I_s$ are the potential difference and current for the secondary coil (all in V and A respectively). Equivalently, the output power is $P_s = V_p \times I_p$.

!!! example "Worked Example (calculation)"

    A transformer in a travel adapter steps up a 115 V ac mains electricity supply to the 230 V needed for a hair dryer. A current of 5 A flows through the hairdryer. Assuming that the transformer is 100% efficient, calculate the current drawn from the mains supply.

    ??? success "Answer:"

        **Step 1: List the known quantities**

        *   Voltage in primary coil, $V_p = 115\text{ V}$

        *   Voltage in secondary coil, $V_s = 230\text{ V}$

        *   Current in secondary coil, $I_s = 5\text{ A}$

        **Step 2: Write the equation linking the known values to the current drawn from the supply, $I_p$**

        $$V_p \times I_p = V_s \times I_s$$

        **Step 3: Substitute in the known values**

        $$115 \times I_p = 230 \times 5$$

        **Step 4: Rearrange the equation to find $I_p$**

        $$I_p = \frac{230 \times 5}{115}$$

        **Step 5: Calculate a value for $I_p$ and include the correct unit**

        $$I_p = 10\text{ A}$$

## Transformers in electricity transmission

Electricity is transmitted through power cables at a low current to minimise energy dissipation: when current flows through a wire, its resistance causes heating, wasting energy to the surroundings — the lower the current, the more efficient the energy transfer. Electrical energy is transferred at **high voltages** from power stations, then at **lower voltages** for domestic use in each locality. To achieve this, the voltage is stepped up by a **step-up** transformer placed **after the power station**, then stepped down by a **step-down** transformer placed **before buildings**, ready for domestic use.

![Diagram showing electricity transmission from a power station to a home via step-up and step-down transformers. Labels include: POWER STATION, INCREASES THE VOLTAGE (25 kV), STEP-UP TRANSFORMER, HIGH VOLTAGE = LOW CURRENT, THIS REDUCES THE POWER LOSS IN TRANSMISSION (400 kV), STEP-DOWN TRANSFORMER, DECREASES THE VOLTAGE (230 V), HOME.](../assets/images/page_407_image_1_v2.jpg)

*Electricity is transmitted at high voltage, reducing the current and hence power loss in the cables using transformers*

!!! tip "Examiner Tips and Tricks"

    Electrical power is equal to voltage × current ($P = V \times I$), so a low current can be achieved for the same power output by increasing the voltage. A **smaller current** flowing through the power lines results in **less heating** in the wire, which **reduces** the **energy loss** in the power cables.

    The key **advantages** of high-voltage transmission of electricity are:

    * The reduced power loss in transmission cables increases the efficiency of energy transfer

    * Lower currents in cables mean thinner, and therefore cheaper, cables can be used
