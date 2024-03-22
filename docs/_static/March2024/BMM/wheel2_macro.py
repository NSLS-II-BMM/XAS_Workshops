######################################################### -*- python -*-
# Cut and paste this line to import your macro after editing:
#
#     %run -i '/nsls2/data3/bmm/XAS/2024-1/313563/2024-03-21//wheel2_macro.py'
#
# Verify that your macro was loaded correctly:
#
#     wheel2_macro??
#
# Then run the macro:
#
#     RE(wheel2_macro())
#                /
############### / #######################################
#              / 
#             /  Note that you are defining a command
#            /   that gets run in BlueSky
#           V
from BMM.suspenders import BMM_suspenders, BMM_clear_suspenders
from BMM.functions import not_at_edge
def wheel2_macro(dryrun=False, ref=False):
    '''User-defined macro for running a sequence of XAFS measurements
    using a standard sample wheel
    '''
    (ok, text) = BMM_clear_to_start()
    if ok is False:
        print(error_msg('\n'+text) + bold_msg('Quitting macro....\n'))
        return(yield from null())

    BMMuser.macro_dryrun = dryrun
    BMMuser.prompt, BMMuser.running_macro = False, True
    BMMuser.instrument = 'double wheel'
    BMM_log_info('Beginning wheel2_macro')
    def main_plan(ref):

        ### ---------------------------------------------------------------------------------------
        ### BOILERPLATE ABOVE THIS LINE -----------------------------------------------------------
        ##  EDIT BELOW THIS LINE
        #<--indentation matters!

        ## change edge before starting, if needed...
        if not_at_edge('Fe', 'K'):
            yield from change_edge('Fe', edge='K', focus=False)

        report("Wheel sequence 1 of 1", level="bold", slack=True)
        yield from slot(18)
        yield from xafs_wheel.outer() # outer ring
        yield from mv(xafs_det, 35.00)
        yield from change_edge('Fe', edge='K', focus=False)
        yield from xafs('wheel2.ini', filename='Fe_Petedunnite', mode='both', element='Fe', sample='Ca(Zn,Mn,Fe,Mg)Si2O6', comment='sample courtesy Martin Stennett, University of Sheffield', times='1 1 1 1')
        close_last_plot()

        if not dryrun:
            BMMuser.running_macro = False
            BMM_clear_suspenders()
            yield from shb.close_plan()


        ##  EDIT ABOVE THIS LINE
        ### BOILERPLATE BELOW THIS LINE -----------------------------------------------------------
        ### ---------------------------------------------------------------------------------------

    def cleanup_plan():
        yield from end_of_macro()
        yield from xafs_wheel.reset()
        (hours, minutes, seconds) = elapsed_time(start)
        report(f'{BMMuser.instrument} macro finished ({hours} hours, {minutes} minutes)', level='bold', slack=True)
        print(bold_msg('[Hint] to start Athena:\t\t') + '%athena')


    start = time.time()
    
    BMM_suspenders()
    yield from finalize_wrapper(main_plan(ref), cleanup_plan())    
    yield from end_of_macro()
    BMM_log_info('wheel2_macro finished!')
