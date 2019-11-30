(defun merge-sort(lst)
  (defun merge_(f s)
    (cond
      ((= (list-length f) 0) s)
      ((= (list-length s) 0) f)
      ((< (car f) (car s)) (append (list (car f)) (merge_ (cdr f) s)))
      ((> (car f) (car s)) (append (list (car s)) (merge_ f (cdr s))))
      ((= (car f) (car s)) (append (list (car f) (car s)) (merge_ (cdr f) (cdr s))))
    )
  )
  (let ((len (list-length lst)))
    (cond
      ((= len 1) lst)
      (t
         (merge_ (merge-sort (subseq lst 0 (ceiling (/ len 2))))
                 (merge-sort (subseq lst (ceiling (/ len 2))))
         )
      )
    )
  )
)

(print (merge-sort (read)))

