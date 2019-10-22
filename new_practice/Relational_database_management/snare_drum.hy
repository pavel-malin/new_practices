(defclass snare-drum ()
())

(defclass cymbal ()
())

(defclass stick ()
())

(defclass brushes ()
())

(defgeneric play (instrument accessory)
  (:documentation "Play sound with instrument and accessory."))


(defmethod play ((instrument snare-drum) (accessory stick))
"POC!")

(defmethod play ((instrument snare-drum) (accessory brushes))
"SHHHH!")

(defmethod play ((instrument cymbal) (accessory brushes))
"FRCCCHT!")

* (play (make-instance 'snare-drum) (make-instance 'stick))
"POC!"

* (play (make-instance 'snare-drum) (make-instance 'brushes))
"SHHH!"