(defun quick_sort(L)
  (cond
    ((null L) nil)
    (t
      (append
        (quick_sort (list< (car L) (cdr L)))
        (cons (car L) nil) 
        (quick_sort (list>= (car L) (cdr L)))))))

(defun list< (a b)
  (cond
    ((or (null a) (null b)) nil)
    ((< a (car b)) (list< a (cdr b)))
    (t (cons (car b) (list< a (cdr b))))))

(defun list>= (a b)
  (cond
    ((or (null a) (null b)) nil)
    ((>= a (car b)) (list>= a (cdr b)))
    (t (cons (car b) (list>= a (cdr b))))))


(print (quick_sort (read)))
