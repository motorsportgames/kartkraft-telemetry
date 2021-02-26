# automatically generated by the FlatBuffers compiler, do not modify

# namespace: KartKraft

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Root object from which all data can be extracted. You must check if motion, dash etc exist before using as not every packet will include all data.
class Frame(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFrame(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Frame()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def FrameBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4B\x4B\x46\x42", size_prefixed=size_prefixed)

    # Frame
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Frame
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Frame
    def Motion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Frame
    def Dash(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = Dashboard()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Frame
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = Session()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Frame
    def VehicleConfig(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = VehicleConfig()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Frame
    def TrackConfig(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = TrackConfig()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Frame
    def SessionConfig(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = SessionConfig()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def FrameStart(builder): builder.StartObject(7)
def FrameAddTimestamp(builder, timestamp): builder.PrependFloat32Slot(0, timestamp, 0.0)
def FrameAddMotion(builder, motion): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(motion), 0)
def FrameAddDash(builder, dash): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(dash), 0)
def FrameAddSession(builder, session): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(session), 0)
def FrameAddVehicleConfig(builder, vehicleConfig): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(vehicleConfig), 0)
def FrameAddTrackConfig(builder, trackConfig): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(trackConfig), 0)
def FrameAddSessionConfig(builder, sessionConfig): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(sessionConfig), 0)
def FrameEnd(builder): return builder.EndObject()
