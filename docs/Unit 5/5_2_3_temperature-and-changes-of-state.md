# Temperature and changes of state

## Naming the changes of state

When a solid is heated, it **melts** to form a liquid: once it reaches the melting point, further energy supplied is transferred to the **potential store** of the particles, breaking the rigid bonds between them so they can flow over each other. When a liquid is heated, it **boils** to form a gas: once it reaches the boiling point, further energy supplied is again transferred to the **potential store** of the particles, this time overcoming the intermolecular bonds completely, so the particles spread far apart and move randomly.

**Evaporation** can also turn a liquid into a gas, but it differs from boiling in three ways: it can happen at any temperature, not just the boiling point; only the most energetic particles at the **surface** of the liquid have enough kinetic energy to escape the intermolecular bonds; and bubbles of gas form in the liquid during boiling, but **not** during evaporation.

!!! info "Classic diagram: changes of state"

    ```mermaid
    graph LR
        subgraph SOLIDS
        S[Particles in a regular lattice]
        end
        subgraph LIQUIDS
        L[Particles close together but random]
        end
        subgraph GASES
        G[Particles far apart and random]
        end

        S -- MELTING --> L
        L -- FREEZING --> S
        L -- BOILING --> G
        G -- CONDENSING --> L
        S -- SUBLIMING --> G
    ```

    *Changing the temperature of a solid, liquid or gas changes its state*

    You should be able to recognise and label a cycle like this one — questions often give this diagram and ask you to name each of the six arrows.

## Core practical 10: investigating changes of state

This experiment aims to investigate how the temperature of ice varies as it changes state from a solid to a liquid.

### Equipment

<table>
  <thead>
    <tr>
        <th>Equipment</th>
        <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Thermometer</td>
        <td>To measure the temperature change of the ice</td>
    </tr>
    <tr>
        <td>Ice cubes</td>
        <td>To investigate temperature changes</td>
    </tr>
    <tr>
        <td>Beaker (400 ml)</td>
        <td>To contain the ice cubes</td>
    </tr>
    <tr>
        <td>Tripod &amp; Gauze</td>
        <td>To support the beaker &amp; ice cubes</td>
    </tr>
    <tr>
        <td>Bunsen Burner</td>
        <td>To heat the beaker &amp; ice</td>
    </tr>
    <tr>
        <td>Stopwatch</td>
        <td>To time the heating process</td>
    </tr>
  </tbody>
</table>

**Resolution of measuring equipment:**

* Thermometer = 0.1 °C

* Stopwatch = 0.1 s

### Method

![Diagram showing apparatus used to heat ice: thermometer, beaker, ice cubes, gauze, tripod, Bunsen burner, and stopwatch showing 00:00](../assets/images/page_330_image_1_v2.jpg)

*Apparatus used to heat ice and measure its temperature as it melts*

1. Place the ice cubes in the beaker (it should be about half full)

2. Place the thermometer in the beaker

3. Place the beaker on the tripod and gauze and slowly start to heat it using the bunsen burner

4. As the beaker is heated, take regular temperature measurements (e.g. at one minute intervals)

5. Continue this whilst the substance changes state (from solid to liquid)

### Results

**An example table of results for the temperature of the ice**

<table>
  <thead>
    <tr>
        <th>Time / s</th>
        <th>Temperature / °C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td colspan="2">0</td>
    </tr>
    <tr>
        <td colspan="2">60</td>
    </tr>
    <tr>
        <td colspan="2">120</td>
    </tr>
    <tr>
        <td colspan="2">180</td>
    </tr>
    <tr>
        <td colspan="2">240</td>
    </tr>
  </tbody>
</table>

### Analysis of results

Plot a graph of the temperature (y-axis) against time (x-axis). The graph will show a region where the temperature of the ice increases, followed by a region with no temperature change even though the ice cubes continue to be heated — this should occur at 0 °C, where the ice is melting from solid to liquid.

<table>
  <thead>
    <tr>
        <th>Time</th>
        <th>Temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Start</td>
        <td>Below 0 °C (Solid)</td>
    </tr>
    <tr>
        <td>Heating</td>
        <td>Increasing (Solid)</td>
    </tr>
    <tr>
        <td>Melting</td>
        <td>Constant at 0 °C</td>
    </tr>
    <tr>
        <td>Post-Melting</td>
        <td>Increasing (Liquid)</td>
    </tr>
  </tbody>
</table>

*A graph of temperature against time will show a flat region where the ice is melting*

### Evaluating the experiment

#### Systematic errors

* Take measurements of temperature from the thermometer at eye level, to avoid parallax errors, and ensure the thermometer is held vertically in the beaker

#### Random errors

* Ensure there are enough ice cubes to surround the thermometer in the beaker, and only begin the experiment when the temperature is below 0 °C, to keep readings of temperature as accurate as possible

#### Safety considerations

* Wear goggles while heating water

* Place the bunsen burner, with the beaker and tripod, on a heatproof mat to avoid surface damage

* Make sure to stand up during the whole experiment, to react quickly to any spills

!!! tip "Examiner Tips and Tricks"

    You might be pleasantly surprised that heat can be transferred to a substance without changing its temperature. This is a very cool effect during changes of state: the **thermal energy** supplied does **not** contribute to the **average kinetic energy** of the particles in the ice - rather, it is used to **weaken the bonds** between the particles so they become freer to slide around each other (i.e. a liquid!). Once the ice is fully melted, the temperature of the liquid water begins rising again.

    Make sure you are familiar with the graph of temperature against time and you can associate the **flat region** with **changing state**

??? info "Beyond the spec: specific latent heat"
    The flat region of the temperature–time graph above shows that energy is still being supplied while the temperature stays constant — that energy is doing work to break (or form) intermolecular bonds, not increasing the particles' kinetic energy. The amount of energy needed to change the state of 1 kg of a substance, without changing its temperature, is called its **specific latent heat**, $L$, measured in J/kg:

    $$\text{energy} = \text{mass} \times \text{specific latent heat} \quad (\Delta Q = mL)$$

    There are two versions of this: the **specific latent heat of fusion** (melting/freezing) and the **specific latent heat of vaporisation** (boiling/condensing) — the same substance has a different value for each, since separating particles completely into a gas takes more energy than merely letting them flow past each other as a liquid. This isn't part of the 4PH1 specification, so it won't come up in an Edexcel IGCSE exam, but it directly extends the specific heat capacity idea from earlier in this unit, and it's exactly the "extra energy" behind this practical's flat region.
