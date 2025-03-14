######################################################### -*- python -*-
# Cut and paste this line to import your macro after editing:
#
#     %run -i '/nsls2/data3/bmm/XAS/2024-1/313563/2024-03-21/sample_macro.py'
#
# Verify that your macro was loaded correctly:
#
#     sample_macro??
#
# Then run the macro:
#
#     RE(sample_macro())
#                /
############### / #######################################
#              / 
#             /  Note that you are defining a command
#            /   that gets run in BlueSky
#           V
from BMM.suspenders import BMM_suspenders, BMM_clear_suspenders
from BMM.functions import not_at_edge
def sample_macro(dryrun=False, ref=False):
    '''User-defined macro for running a sequence of XAFS measurements
    using (example...)
    '''
    (ok, text) = BMM_clear_to_start()
    if ok is False:
        print(error_msg('\n'+text) + bold_msg('Quitting macro....\n'))
        return(yield from null())

    BMMuser.macro_dryrun = dryrun
    BMMuser.prompt, BMMuser.running_macro = False, True
    BMMuser.instrument = ''
    BMM_log_info('Beginning sample_macro')
    def main_plan(ref):

        ### ---------------------------------------------------------------------------------------
        ### BOILERPLATE ABOVE THIS LINE -----------------------------------------------------------
        ##  EDIT BELOW THIS LINE
        #<--indentation matters!


        ## sample 1
        yield from slot(1)
        yield from xafs('scan.ini', filename='samp1', sample='first sample')
        close_last_plot()
    
        ## sample 2
        yield from slot(2)
        ## yield from mvr(xafs_x, 0.5)
        yield from xafs('scan.ini', filename='samp2', sample='another sample', comment='my comment')
        close_last_plot()

        ## sample 3
        yield from slot(3)
        yield from xafs('scan.ini', filename='samp3', sample='a different sample', prep='this sample prep', nscans=4)
        close_last_plot()

        ##  EDIT ABOVE THIS LINE
        ### BOILERPLATE BELOW THIS LINE -----------------------------------------------------------
        ### ---------------------------------------------------------------------------------------

    def cleanup_plan():
        yield from end_of_macro()
        
        (hours, minutes, seconds) = elapsed_time(start)
        report(f'{BMMuser.instrument} macro finished ({hours} hours, {minutes} minutes)', level='bold', slack=True)
        print(bold_msg('[Hint] to start Athena:\t\t') + '%athena')


    start = time.time()
    
    BMM_suspenders()
    yield from finalize_wrapper(main_plan(ref), cleanup_plan())    
    yield from end_of_macro()
    BMM_log_info('sample_macro finished!')
