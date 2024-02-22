import marshal
myfile = input("wirte path file:")
open_file=open(myfile,"r").read()
compile_file=compile(open_file, '', 'exec')
encrypt=marshal.dumps(compile_file)
code = open('New'+str(myfile),'w')
code.write("import marshalkey \n")
code.write('exec(marshal.loads('+repr(encrypt)+'))')
print("The file Ecrypted: "+str(myfile))