class O: ...
class A(O): ...
class B(O): ...
class C(O): ...
class D(O): ...
class E(O): ...

class K1(A, B, C): ...
class K2(B, D): ...
class K3(C, D, E): ...

class Z(K1, K2, K3): ...

