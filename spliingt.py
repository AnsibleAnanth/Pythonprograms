fid = fopen('yourfile.txt', 'r')
NperSet = 72E6
ix = 0
while ~feof(fid)
ix = ix+1
data = cell2mat(textscan(fid, '%\t%f', NperSet))
    stats(ix, :) = [mean(data) std(data) ...]

end
