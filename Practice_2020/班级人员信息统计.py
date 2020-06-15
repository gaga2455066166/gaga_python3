ac = input();
bc = input();
acm = input();
eng = input();
zz = input();

as1 = set(ac);
bs1 = set(bc.split(' '));
acm2 = set(acm.split(' '));
eng2 = set(eng.split(' '));

if '' in bs1:
  bs1.remove('');
if '' in acm2:
  acm2.remove('');
if '' in eng2:
  eng2.remove('');

#人数
print('Total: '+str(len(as1)+len(bs1)));
#不参加竞赛的
notrace = list();
for temp in as1:
    if temp not in acm2 and temp not in eng2:
        notrace.append(temp);
for temp in bs1:
    if temp not in acm2 and temp not in eng2:
        notrace.append(temp);
print('Not in race: '+str(sorted(notrace))+', num: '+str(len(notrace)));
#所有参赛的
allracers = list();
for temp in as1:
    if temp in acm2 or temp in eng2:
        allracers.append(temp);
for temp in bs1:
    if temp in acm2 or temp in eng2:
        allracers.append(temp);
print('All racers: '+str(sorted(allracers))+', num: '+str(len(allracers)));
#都参加了的
both = list();
for temp in as1:
    if temp in acm2 and temp in eng2:
        both.append(temp);
for temp in bs1:
    if temp in acm2 and temp in eng2:
        both.append(temp);
print('ACM + English: '+str(sorted(both))+', num: '+str(len(both)));
#只参加了ACM的
acm3 = list();
for temp in as1:
    if temp in acm2 and temp not in eng2:
        acm3.append(temp);
for temp in bs1:
    if temp in acm2 and temp not in eng2:
        acm3.append(temp);
print('Only ACM: '+str(sorted(acm3)));
#只参加了英语的
eng3 = list();
for temp in as1:
    if temp not in acm2 and temp in eng2:
        eng3.append(temp);
for temp in bs1:
    if temp not in acm2 and temp in eng2:
        eng3.append(temp);
print('Only English: '+str(sorted(eng3)));
#只参加ACM或英语的
dd = eng3+acm3;
print('ACM Or English: '+str(sorted(dd)));
#判断转学
if zz in as1:
    new = list(as1);
    new.remove(zz)
    print(sorted(new));
elif zz in bs1:
    new = list(bs1);
    new.remove(zz);
    print(sorted(new));