## Definitions
**Backseat driver**: the software that mediates the updating of data and values of glider flight cpu (F-CPU) with information from glider science cpu
**External controller:** user defined script that provides input and reads output over Glider's Science CPU (S-CPU)
**Sensor:** value stored on one of the glider's CPUs

**Sensor**
A value stored on the glider. Doesn't guarantee that there is a piece of hardware making the measurement. 
- sci_* : science sensors
- u_* : user defined, typically before runtime. u_mission_param_* is a special case which may change during a mission

**Backseat driver**
The FCPU queries the SCPU for sensor values, and makes adjustments to its trajectory if discrepancy or specified to do so. This provides for more accurate dead reckoning. Also gives users the ability to update certain b_args based on science sensor values

**F-CPU implementation**
- 12 user sensors (u_mission_param_* ) which can be modified by S-CPU through external inputs
- flight behaviors can be modified by linking u_mission_param to a b_arg and updating mid-mission (by SCPU)
- u_mission_params are linked to b_args with special values 1,000,000 to 1,000,011 (12 total)

**S-CPU implementation**
- extcl proglet designed to send + receive messages over UART ports on S-CPU
	- is this the same as extctl.ini?