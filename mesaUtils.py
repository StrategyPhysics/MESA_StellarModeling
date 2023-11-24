import re   # regex
import matplotlib.pyplot as plt

def get_mesaConfig (mesaIndex):
    f = open(mesaIndex, 'r')
    mesaConfig = {}
    
    # First line requires special handling to extract the run number
    first_line = f.readline()
    job = re.search(r'\d{11}', first_line)
    mesaConfig['Job'] = job.group(0).strip()

    # Pull out the rest of the key:value pairs
    for line in f:
        listedline = line.strip().split(':', 1) # split around the = sign
        if len(listedline) > 1: # we have the = sign in there
            #print(listedline[0].strip(), listedline[1].strip())
            mesaConfig[listedline[0].strip()] = listedline[1]  #.strip()
    return mesaConfig

def plotMesa(folder_name, mesaConfig,hist):
    report_title = str(folder_name) +  '  | ' + str(mesaConfig['Initial Mass'])

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10,12)) # figsize=(10,5)
    fig.suptitle(report_title, fontsize=16)

    ax1.plot(hist['log_Teff'], hist['log_L']); ax1.set_xlabel('log(T/K)'); ax1.set_ylabel('log (L/Lsun)'), ax1.set_title('HR Diagram')
    ax1.invert_xaxis()

    ax2.plot(hist['star_age']/1E9, hist['center_h1'], color='b', label='Xc - Hydrogen')
    ax2.plot(hist['star_age']/1E9, hist['center_he4'], color='r', label='Yc - Helium 4')
    ax2.set_xlabel('Age (Gyr)'); ax2.set_title('H Depletion'); ax2.legend()

    ax3.plot(hist['star_age']/1e9, hist['log_Teff']); ax3.set_xlabel('Age (Gyr)'); ax3.set_ylabel('log(T/K)')
    ax3.set_title('Temperature Evolution')

    ax4.plot(hist['star_age']/1e9, hist['log_L']); ax4.set_xlabel('Age (Gyr)'); ax4.set_ylabel('log(L/Lsun)')
    ax4.set_title('Luminosity Evolution')
    
    return