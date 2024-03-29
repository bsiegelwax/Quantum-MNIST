from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_data = QuantumRegister(8, 'data')
qreg_test = QuantumRegister(8, 'test')
qreg_a = QuantumRegister(1, 'a')
creg_c = ClassicalRegister(10, 'c')
circuit = QuantumCircuit(qreg_data, qreg_test, qreg_a, creg_c)

circuit.u3(0.00028395*pi, 0.450122743*pi, 0, qreg_data[0])
circuit.u3(0.069290492*pi, 0.026794555*pi, 0, qreg_data[1])
circuit.u3(0.184908494*pi, 0.182222767*pi, 0, qreg_data[2])
circuit.u3(0.012726233*pi, 0.389883137*pi, 0, qreg_data[3])
circuit.u3(0.115369005*pi, 0.259224751*pi, 0, qreg_data[4])
circuit.u3(0.389950429*pi, 0.01595724*pi, 0, qreg_data[5])
circuit.u3(0.365638092*pi, 0.002353676*pi, 0, qreg_data[6])
circuit.u3(0.138996987*pi, 0.153243011*pi, 0, qreg_data[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.00000641666*pi, 0.082324313*pi, 0, qreg_data[0])
circuit.u3(0.02098256*pi, 0.000199622*pi, 0, qreg_data[1])
circuit.u3(0.106801487*pi, 0.002681601*pi, 0, qreg_data[2])
circuit.u3(0.00513601*pi, 0.36268689*pi, 0, qreg_data[3])
circuit.u3(0.000375199*pi, 0.12306639*pi, 0, qreg_data[4])
circuit.u3(0.243523806*pi, 0.002681883*pi, 0, qreg_data[5])
circuit.u3(0.21331916*pi, 0.000285577*pi, 0, qreg_data[6])
circuit.u3(0.000597948*pi, 0.063131156*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.003840916*pi, 0.161781689*pi, 0, qreg_data[0])
circuit.u3(0.16219387*pi, 0.011832873*pi, 0, qreg_data[1])
circuit.u3(0.208302391*pi, 0.031324933*pi, 0, qreg_data[2])
circuit.u3(0.006227607*pi, 0.406946267*pi, 0, qreg_data[3])
circuit.u3(0.061525773*pi, 0.164838494*pi, 0, qreg_data[4])
circuit.u3(0.491109622*pi, 0.022745765*pi, 0, qreg_data[5])
circuit.u3(0.476289586*pi, 0.019381086*pi, 0, qreg_data[6])
circuit.u3(0.08265182*pi, 0.091967562*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.007140282*pi, 0.287102485*pi, 0, qreg_data[0])
circuit.u3(0.155974707*pi, 0.018853482*pi, 0, qreg_data[1])
circuit.u3(0.155030408*pi, 0.014377711*pi, 0, qreg_data[2])
circuit.u3(0.003839239*pi, 0.482518156*pi, 0, qreg_data[3])
circuit.u3(0.028075072*pi, 0.269478484*pi, 0, qreg_data[4])
circuit.u3(0.176019953*pi, 0.027634341*pi, 0, qreg_data[5])
circuit.u3(0.434067647*pi, 0.003693121*pi, 0, qreg_data[6])
circuit.u3(0.035396099*pi, 0.193683335*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.001949048*pi, 0.325607881*pi, 0, qreg_data[0])
circuit.u3(0.024086865*pi, 0.028454152*pi, 0, qreg_data[1])
circuit.u3(0.05217044*pi, 0.04487954*pi, 0, qreg_data[2])
circuit.u3(0.017645592*pi, 0.365554205*pi, 0, qreg_data[3])
circuit.u3(0.034988578*pi, 0.062312257*pi, 0, qreg_data[4])
circuit.u3(0.373700356*pi, 0.000386305*pi, 0, qreg_data[5])
circuit.u3(0.477215408*pi, 0.003850176*pi, 0, qreg_data[6])
circuit.u3(0.023517024*pi, 0.126362154*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.000325601*pi, 0.428772316*pi, 0, qreg_data[0])
circuit.u3(0.052706643*pi, 0.007629778*pi, 0, qreg_data[1])
circuit.u3(0.131670605*pi, 0.07149694*pi, 0, qreg_data[2])
circuit.u3(0.04144115*pi, 0.313279213*pi, 0, qreg_data[3])
circuit.u3(0.027317564*pi, 0.23176903*pi, 0, qreg_data[4])
circuit.u3(0.237508277*pi, 0.011494194*pi, 0, qreg_data[5])
circuit.u3(0.359229521*pi, 0.00313704*pi, 0, qreg_data[6])
circuit.u3(0.025402269*pi, 0.169682492*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.00058562*pi, 0.365998424*pi, 0, qreg_data[0])
circuit.u3(0.10185285*pi, 0.007896353*pi, 0, qreg_data[1])
circuit.u3(0.167904406*pi, 0.040345073*pi, 0, qreg_data[2])
circuit.u3(0.008246305*pi, 0.219654877*pi, 0, qreg_data[3])
circuit.u3(0.01788256*pi, 0.077303155*pi, 0, qreg_data[4])
circuit.u3(0.536463771*pi, 0.000593473*pi, 0, qreg_data[5])
circuit.u3(0.572379933*pi, 0.000731566*pi, 0, qreg_data[6])
circuit.u3(0.10364839*pi, 0.075730167*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.001005149*pi, 0.367059042*pi, 0, qreg_data[0])
circuit.u3(0.016033028*pi, 0.054132548*pi, 0, qreg_data[1])
circuit.u3(0.015459258*pi, 0.036050218*pi, 0, qreg_data[2])
circuit.u3(0.000856296*pi, 0.503759403*pi, 0, qreg_data[3])
circuit.u3(0.006050514*pi, 0.195151679*pi, 0, qreg_data[4])
circuit.u3(0.112316911*pi, 0.003452509*pi, 0, qreg_data[5])
circuit.u3(0.389298443*pi, 0.000460729*pi, 0, qreg_data[6])
circuit.u3(0.007621025*pi, 0.129712118*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.000429905*pi, 0.41596236*pi, 0, qreg_data[0])
circuit.u3(0.069861127*pi, 0.01009603*pi, 0, qreg_data[1])
circuit.u3(0.159855729*pi, 0.073479905*pi, 0, qreg_data[2])
circuit.u3(0.014303956*pi, 0.461282254*pi, 0, qreg_data[3])
circuit.u3(0.006485058*pi, 0.239033601*pi, 0, qreg_data[4])
circuit.u3(0.39857635*pi, 0.005580055*pi, 0, qreg_data[5])
circuit.u3(0.387985338*pi, 0.0026321*pi, 0, qreg_data[6])
circuit.u3(0.013359594*pi, 0.191111681*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])
circuit.measure(qreg_a[0], creg_c[8])
circuit.barrier(qreg_data[0], qreg_data[1], qreg_data[2], qreg_data[3], qreg_data[4], qreg_data[5], qreg_data[6], qreg_data[7])
circuit.barrier(qreg_test[0], qreg_test[1], qreg_test[2], qreg_test[3], qreg_test[4], qreg_test[5], qreg_test[6], qreg_test[7])
circuit.reset(qreg_data[0])
circuit.reset(qreg_data[1])
circuit.reset(qreg_data[2])
circuit.reset(qreg_data[3])
circuit.reset(qreg_data[4])
circuit.reset(qreg_data[5])
circuit.reset(qreg_data[6])
circuit.reset(qreg_data[7])
circuit.u3(0.0000217332*pi, 0.40389579*pi, 0, qreg_data[0])
circuit.u3(0.018071213*pi, 0.014602313*pi, 0, qreg_data[1])
circuit.u3(0.047342227*pi, 0.024634393*pi, 0, qreg_data[2])
circuit.u3(0.000915173*pi, 0.476446991*pi, 0, qreg_data[3])
circuit.u3(0.01224006*pi, 0.104939022*pi, 0, qreg_data[4])
circuit.u3(0.275367868*pi, 0.001861994*pi, 0, qreg_data[5])
circuit.u3(0.441123843*pi, 0.004107887*pi, 0, qreg_data[6])
circuit.u3(0.006326019*pi, 0.172366667*pi, 0, qreg_data[7])
circuit.reset(qreg_test[0])
circuit.reset(qreg_test[1])
circuit.reset(qreg_test[2])
circuit.reset(qreg_test[3])
circuit.reset(qreg_test[4])
circuit.reset(qreg_test[5])
circuit.reset(qreg_test[6])
circuit.reset(qreg_test[7])
circuit.u3(0*pi, 0.380152061*pi, 0, qreg_test[0])
circuit.u3(0.00040016*pi, 0.008643457*pi, 0, qreg_test[1])
circuit.u3(0.003441377*pi, 0.23777511*pi, 0, qreg_test[2])
circuit.u3(0*pi, 0.104521809*pi, 0, qreg_test[3])
circuit.u3(0.124529812*pi, 0*pi, 0, qreg_test[4])
circuit.u3(0.349819928*pi, 0*pi, 0, qreg_test[5])
circuit.u3(0.270908363*pi, 0*pi, 0, qreg_test[6])
circuit.u3(0.202641056*pi, 0*pi, 0, qreg_test[7])
circuit.reset(qreg_a[0])
circuit.h(qreg_a[0])
circuit.cswap(qreg_a[0], qreg_test[0], qreg_data[0])
circuit.cswap(qreg_a[0], qreg_test[1], qreg_data[1])
circuit.cswap(qreg_a[0], qreg_test[2], qreg_data[2])
circuit.cswap(qreg_a[0], qreg_test[3], qreg_data[3])
circuit.cswap(qreg_a[0], qreg_test[4], qreg_data[4])
circuit.cswap(qreg_a[0], qreg_test[5], qreg_data[5])
circuit.cswap(qreg_a[0], qreg_test[6], qreg_data[6])
circuit.cswap(qreg_a[0], qreg_test[7], qreg_data[7])
circuit.h(qreg_a[0])