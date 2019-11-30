;function for linear search and return the position of item in the list
(defun linear_search(list_ item)
       (loop for pos from 0 and element in list_
             when(eql item element)
                do(return (+ pos 1))
             )
)


(print (linear_search (list 1 2 4 5 6 7 8) 2))
