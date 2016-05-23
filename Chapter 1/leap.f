pure elemental function leap_year(y) result(is_leap)
	implicit none
	logical :: is_leap
	integer,intent(in) :: y	
 
	is_leap = (mod(y,4)==0 .and. .not. mod(y,100)==0) .or. (mod(y,400)==0)	
 
end function leap_year
