if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

PS1='\[\e[1;33m\]\u\[\e[1;37m\]@\[\e[1;34m\]\h\[\e[1;37m\]:\[\e[1;32m\]\w\[\e[1;37m\] \$\[\e[0;37m\] ';
