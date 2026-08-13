# Circuit laws

There are two ways of joining electrical components: in **series**, or in **parallel**.

## Current

### Current in series

A **series** circuit is a circuit that has only one loop, or one path that the electrons can take. In a series circuit, the current has the **same value at any point**, because the electrons have only one path they can take — the number of electrons passing a fixed point per unit time is the same at all locations. This means **all** components in a series circuit have the same current.

![Circuit diagram showing a battery, two lamps, and three ammeters all reading 0.3 A in a single loop.](../assets/images/page_132_image_1_v2.jpg)

*The current is the same at each point in a series circuit*

The amount of current flowing in a series circuit depends on the **voltage** of the power source, and the **number** (and type) of components. **Increasing** the **voltage** of the power source drives **more current** around the circuit (so decreasing the voltage reduces the current), while **increasing** the **number** of components in the circuit **increases** the **total resistance**, so **less current** flows through the circuit.

![Diagram showing how current changes with voltage and number of components in a circuit. Top half shows that more voltage leads to more current. Bottom half shows that more components lead to less current.](../assets/images/page_133_image_1_v2.jpg)

*Current will increase if the voltage of the power supply increases and decreases if the number of components increases*

### Current in parallel

A parallel circuit is a circuit that has two or more loops, or more than one path that electrons can take. Parallel circuits contain **junctions** (points where two or more wires meet to form a new branch) and **branches** (the sections of wire between junctions). In a parallel circuit, the current has different values at different points, because the current **splits** at a junction, so the electrons have different paths they can take. The **sum** of the current in the **individual** branches is equal to the total current before (and after) the branches.

![Diagram showing current splitting and recombining at junctions. On the left, current I1 + I2 enters a junction and splits into I1 and I2. On the right, currents I1 and I2 enter a junction and recombine into I1 + I2.](../assets/images/page_134_image_1_v2.jpg)

*Current splits at a junction into individual branches*

At a junction, the current is always **conserved**: the amount of current flowing into the junction is equal to the amount flowing out of it, because **charge** is conserved. Current does not always split equally — often there will be more current in some branches than in others, and the current in each branch will only be identical if the resistance of the components along each branch is **identical**. Current behaves this way because it is the **flow of electrons**: electrons, or any charge, cannot be created or destroyed, so the total number of electrons (and hence current) going around a circuit must remain the same — when the electrons reach a junction, however, some go one way and the rest go the other.

!!! example "Worked Example (calculation)"

    In the circuit below, ammeter A<sub>0</sub> shows a reading of 10 A, and ammeter A<sub>1</sub> shows a reading of 6 A.

    ![Circuit diagram showing a battery and three parallel branches with ammeters A0, A1, and A2.](../assets/images/page_135_image_1_v2.jpg)

    What is the reading on ammeter A<sub>2</sub>?

    ??? success "Answer:"

        **Step 1: Recall what happens to the current at a junction**

        At a junction, the current splits, but is always conserved — the total amount of current flowing into a junction is equal to the total amount flowing out.

        **Step 2: Consider the first junction in the circuit where the current splits**

        The diagram below shows the first junction in the circuit:

        ![Diagram of a circuit junction showing 10 A flowing in, and splitting into 6 A through ammeter A1 and 4 A (in red) through the other branch.](../assets/images/page_135_image_2_v2.jpg)

        **Step 3: Calculate the missing amount of current**

        Since 10 A flows into the junction (the total current from the battery), 10 A must flow out of the junction. The question says that 6 A flows through ammeter A<sub>1</sub>, so the remaining current flowing through ammeter A<sub>2</sub> must be:

        $$ 10\text{ A} - 6\text{ A} = 4\text{ A} $$

        Therefore, **4 A** flows through ammeter A<sub>2</sub>.

!!! tip "Examiner Tips and Tricks"

    The direction of current flow is super important when considering junctions in a circuit.

    You should remember that current flows from the **positive** terminal to the **negative** terminal of a cell / battery. This will help determine the direction current is flowing 'in' to a junction and which way the current then flows 'out'.

    ```mermaid
    graph LR
        A[+] --- B[CONDUCTOR]
        B --- C[-]
        subgraph " "
        direction LR
        D[FLOW OF CHARGE] --> E[ ]
        style E fill:none,stroke:none
        end
        style A fill:#f28b82,stroke:#000
        style B fill:#bdbdbd,stroke:#000
        style C fill:#81d4fa,stroke:#000
        style D fill:#b9f6ca,stroke:#000
    ```

## Voltage

### Voltage in series

In a series circuit, the **total voltage** of a power supply is **shared** between the components.

![Circuit diagram showing a 12 V battery connected in series to two identical lamps with resistance R, each having a 6 V potential difference across them.](../assets/images/page_137_image_1_v2.jpg)

*Lamps connected in a series circuit share the potential difference from the battery*

For two identical components (with equal resistance), the voltage across them will be the **same**, and equal to **half the total voltage** of the power supply. For two non-identical components (with different resistance), the voltage will be **higher** across the component with the higher resistance, and **lower** across the component with lower resistance.

### Voltage in parallel

In a parallel circuit, the **total voltage** across each branch is the **same** as the voltage of the power supply.

![Circuit diagram showing two lamps in parallel with a 12V battery, indicating current I1 + I2 and 12V across each lamp.](../assets/images/page_138_image_2_v2.jpg)

*Lamps connected in a parallel circuit all have the same voltage across them*

## Resistance

### Resistors in series

When two or more resistors are connected in series, the **total resistance** is equal to the **sum** of their individual resistances. For two resistors of resistance $R_1$ and $R_2$, the total resistance can be calculated using the equation $R = R_1 + R_2$, where $R$ is the total resistance in ohms (Ω). Increasing the number of resistors **increases** the overall resistance, since the charge now has **more** resistors to pass through — the **total voltage** is also the **sum** of the voltages across each of the individual resistors.

![Circuit diagram showing three resistors R1, R2, and R3 in series with voltmeters V1, V2, and V3 connected across each](../assets/images/page_141_image_2_v2.jpg)

Total voltage $= V_1 + V_2 + V_3$; combined resistance $= R_1 + R_2 + R_3$.

*Three resistors connected in series. The total voltage is the sum of the individual voltages, and the total resistance is the sum of the three individual resistances*

### Summary of series and parallel circuits

For components connected in **series**: the **current** is the same at all points and in each component, the **voltage** of the power supply is shared between the components, and the **total resistance** is the sum of the resistances of each component.

For components connected in **parallel**: the **current** from the supply splits between the branches, the **voltage** across each branch is the same, and the **total resistance** is less than that of each component.

!!! example "Worked Example (multiple choice)"

    The combined resistance $R$ in the following series circuit is 60 Ω.

    What is the resistance value of $R_2$?

    ![Circuit diagram showing a battery and three resistors in series: R1 = 30 Ω, R2, and R3 = 10 Ω.](../assets/images/page_142_image_1_v2.jpg)

    **A** 100 Ω      **B** 30 Ω      **C** 20 Ω      **D** 40 Ω

    ??? success "Answer: C"

        **Step 1: Write down the equation for the combined resistance in series**

        $$R = R_1 + R_2 + R_3$$

        **Step 2: Substitute the values for total resistance $R$ and the other resistors**

        $$60\ \Omega = 30\ \Omega + R_2 + 10\ \Omega$$

        **Step 3: Rearrange for $R_2$**

        $$R_2 = 60\ \Omega - 30\ \Omega - 10\ \Omega = \mathbf{20\ \Omega}$$

!!! example "Worked Example (calculation)"

    Dennis sets up a series circuit as shown below.

    ![Circuit diagram showing a cell, an ammeter (A), a variable resistor, a fixed resistor, and a voltmeter (V) in parallel with the fixed resistor.](../assets/images/page_143_image_1_v2.jpg)

    The cell supplies a current of 2 A to the circuit, and the fixed resistor has a resistance of 4 Ω.

    (a) How much current flows through the fixed resistor?

    (b) What is the reading on the voltmeter?

    ??? success "Answer (Part a):"

        Current is conserved in a series circuit, so it is the same size measured anywhere in the loop. Since the cell supplies 2 A to the circuit, the current is 2 A everywhere — therefore, **2 A** flows through the fixed resistor.

    ??? success "Answer (Part b):"

        **Step 1: List the known quantities**

        * Current, $I = 2\text{ A}$

        * Resistance, $R = 4\text{ }\Omega$

        **Step 2: State the equation linking potential difference, resistance and current**

        $$V = I \times R$$

        **Step 3: Substitute the known values into the equation and calculate the potential difference**

        $$V = 2 \times 4 = 8\text{ V}$$

        Therefore, the voltmeter reads **8 V** across the fixed resistor.
