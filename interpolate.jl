using Dierckx

function interpolate(x::Array{Float64}, y::Array{Float64}, k::Array{Float64})
  spline = Spline1D(x, y; w=ones(length(x)), k=2, bc="nearest", s=0.0)
  array = spline(k)
  return array[:]
end
